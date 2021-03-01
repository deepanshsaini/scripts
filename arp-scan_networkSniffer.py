import sys
import subprocess
import os
import time
from datetime import datetime

#password
password = 'yourPasswordGoesHere'

#creating an empty list for graphs use 
history_devices = []
history_time = [] 

#Creating a empty file to save output 
output_file = open("/Users/deepanshsaini/Desktop/output_history.txt",'a')
graph_file = open("/Users/deepanshsaini/Desktop/graph.csv",'a')
graph_file.write("Connected_Devices,Time\n")

#installing arp-scan of not present
def install(package):
    sudoPassword = password
    command = 'sudo apt-get update -y'
    os.system('echo %s|sudo -S %s' % (sudoPassword, command))
    command = 'sudo apt-get upgrade -y'
    os.system('echo %s|sudo -S %s' % (sudoPassword, command))
    try:
        command = 'sudo apt-get install arp-scan'
        os.system('echo %s|sudo -S %s' % (sudoPassword, command))
    except subprocess.CalledProcessError as e:
        print(e)

def network_sniffing():
    #Checking if the module exists 
    sudo_password = password
    command = 'arp-scan -l'
    p = os.system('echo %s|sudo -S %s' % (sudo_password, command))

    if p == 0 :
        command = 'arp-scan -l'
        command = command.split()
        

        cmd1 = subprocess.Popen(['echo',sudo_password], stdout=subprocess.PIPE)
        cmd2 = subprocess.Popen(['sudo','-S'] + command, stdin=cmd1.stdout, stdout=subprocess.PIPE)

        output = cmd2.stdout.read().decode() 

        #extracting the number of connected devices
        connected_devices = output[-12:-10]          #Getting the exact no devices connected to network from python
        int(connected_devices)                       #Converting into int 
        print(connected_devices)

        #getting current date and time 
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %I:%M:%S %p")
        print("Date and Time = ", dt_string)


        #Upadting values of a list
        history_devices.append(connected_devices)
        history_time.append(dt_string)

        #saving all output in a file
        output_file.write(f"{output} {dt_string} ")
        output_file.flush()
        
        graph_file.write(f"{connected_devices},{dt_string}\n") #file for the no of connected devices and time for further study
        graph_file.flush()
    else:
        print("The package is not installed")
        


#_____________main________________

count = 1
while count > 0:
    network_sniffing()
    #time.sleep(5)



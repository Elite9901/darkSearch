import socket
import subprocess
import sys
from datetime import datetime
# Clear the screen
subprocess.call('clear', shell=True)

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

prGreen("====================================================")
prGreen("====================================================")
prRed("=================== DARK SEARCH ===================")
prGreen("================ Author: Eli Hacks =================")
prYellow("===================================================")
prYellow("===================================================")
# Ask for input
remoteServer=input(" [✓] Enter a remote host to scan: ")
remoteServerIP=socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan
prCyan("-" * 60)
print("Please wait, scanning remote host", remoteServerIP)
prCyan("-" * 60)

# Check what time the scan started
t1 = datetime.now()

# Using the range function to specify ports (here it will scans all ports between 1 and 1024)

# We also put in some error handling for catching errors

try:
    for port in range(1,1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}: 	 Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    prRed("Hostname could not be resolved. Exiting")
    sys.exit()

except socket.error:
    prRed("Couldn't connect to server")
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
prGreen("Scanning Completed in: ", total)

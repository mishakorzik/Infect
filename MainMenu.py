import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd Infect && bash src/Logo.sh")

print("  \033[1;34m[1] >> \033[1;36;40mInfect")
print("  \033[1;34m[2] >> \033[1;36;40mUpdate")
print("  \033[1;34m[3] >> \033[1;36;40mAbout")
print("  \033[1;34m[4] >> \033[1;36;40mExit")

op=int(raw_input("1nfEct: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd Infect && bash src/Logo.sh && python2 src/InfectMenu.py")
elif(op==2):
 os.system("clear")
 os.system("cd")
elif(op==3):
 time.sleep(0.2)
 os.system("cd && cd Infect && bash src/About.sh")
elif(op==4):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting utility...")
 os.system("cd")
else:
 print("\033[1;31;40mInvalid input. Reloading Tool") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd Infect")
 os.system("python2 MainMenu.py")

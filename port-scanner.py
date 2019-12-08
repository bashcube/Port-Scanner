import sys
import os
import socket 

os.system('clear')

print ("                  _                                            ")
print (" _ __   ___  _ __| |_      ___  ___ __ _ _ __  _ __   ___ _ __ ")
print ("| '_ \ / _ \| '__| __|____/ __|/ __/ _` | '_ \| '_ \ / _ \ '__|")
print ("| |_) | (_) | |  | ||_____\__ \ (_| (_| | | | | | | |  __/ |   ")
print ("| .__/ \___/|_|   \__|    |___/\___\__,_|_| |_|_| |_|\___|_|   ")
print ("|_|")       
print ()

print ("1.Domain name")
print ("2.IP-Address")
input_choice = int(input("Enter choice: "))
print()

if input_choice == 1:
	input_domain = input("Enter domain name: ")
	try:
		ip_addr = socket.gethostbyname(input_domain)
	except:
		print ("Unable to resolve IP from domain name.")
		sys.exit()
else:
	ip_addr = input("Enter IP Address: ")
print()

min = int(input("Enter port (where scan will start): "))
max = int(input("Enter port (where scan will stop): "))
print()

if max < min:
	print ("Unable to scan for the given range of ports.")
	sys.exit()

for i in range (min, max+1):
	con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	if con.connect_ex((ip_addr,i))== 0:
		print ("Port{}:Open".format(i))
	con.close()
print ()
	


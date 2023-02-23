

import pyfiglet
import socket
from termcolor import colored
banner = colored(pyfiglet.figlet_format(" FIND * IP"),'green')
print(banner)

domin_name = input("Enter your domin name: ")
ip = socket.gethostbyname(domin_name)

print(ip)
print(ip)
print(ip)
print()
print()
print()

name = ("create by scope BuG")
print(name)


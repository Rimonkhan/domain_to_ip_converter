#! /usr/bin/env python3
import socket
from termcolor import colored
import pyfiglet
import os
print("******************************** Cyber Hacker ********************************")
print(colored("******************************** CREATE BY HACK ZONE ********************************",color="red"))

systeminfo = os.system('date')
tool_details = colored(pyfiglet.figlet_format("Domain to ip"),color="green")
print(tool_details)
print(colored(pyfiglet.figlet_format("CYber"),color="red"))

print(colored("******************************** Cyber Hacker ********************************",color="green"))

domainName=input("Enter your domain name : ")
Ip_Convert = socket.gethostbyname(domainName)
print(f"{domainName} is ip : ",Ip_Convert)

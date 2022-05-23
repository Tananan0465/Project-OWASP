import socket
from subprocess import PIPE, run
import os

def getipfromhost(url):
    hostname = open(url, "r").read()
    if hostname[-1] == '/':
        hostname = hostname[:-1]
    if "http://" in hostname:
        hostname = hostname[7:]
    if "https://" in hostname:
        hostname = hostname[8:]
    IPAddr = socket.gethostbyname(hostname)
    host = open("./temp/url_temp.txt", "w")
    host.write(hostname)
    host.close()
    print("URL: " + hostname)   
    ip = open("./temp/ip_temp.txt", "w")
    ip.write(IPAddr)
    ip.close()
    print("IP Address: " + IPAddr)
    print()


    
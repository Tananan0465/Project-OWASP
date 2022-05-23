from json.tool import main
from scripts.script_dirsearch import directoryListing
from scripts.script_ssl import ssl
from scripts.script_scanport import scanport
from scripts.getip import getipfromhost
from scripts.script_xss import xssmain
import socket
from scripts.genDir import genDir
import os

state = True


def program():
    print("\nPlease choose a command to test vulnerability.")
    print("Command:")
    print("\t-a, --all\t\tTest all command.")
    print("\t-d, --directory\t\tDirectory Listing")
    print("\t-p, --portscan\t\tScan open port")
    print("\t-s, --ssl\t\tInsecure SSL/TLS Configuration")
    print("\t-x, --xss\t\tCross-site scripting (XSS)")
    print("\t--chu\t\t\tChange URL.")
    print("\t--exit\t\t\tClose program.\n")

    if os.stat("url.txt").st_size == 0:
        print("Please enter URL !!!")
        command = "--chu"
    else:
        getipfromhost("url.txt")
        url = "./temp/url_temp.txt"
        ip = "./temp/ip_temp.txt"
        genDir()
        command = input("input command: ")

    cmdlist = ['-a', '--all', '-d', '--directory',
            '-p', '--portscan', '-s', '--ssl', '-x', '--xss', '--chu']
    closelist = ['--exit']

    if command in cmdlist:
        if command == '-a' or command == '--all':
            print("Vulnerability : All")
            scanport(ip)
            xssmain(url)
            ssl(url)
            directoryListing(url)
            print("Process Completed !!!")
            print("------------------------------")
            
        elif command == '-d' or command == '--directory':
            print("Vulnerability : Directory Listing")
            directoryListing(url)

        elif command == '-p' or command == '--portscan':
            print("Vulnerability : Scan open port")
            scanport(ip)  # ip only

        elif command == '-s' or command == '--ssl':
            print("Vulnerability : Insecure SSL/TLS Configuration")
            ssl(url)  # url no-protocol

        elif command == '-x' or command == '--xss':
            print("Vulnerability : Cross-site scripting (XSS)")
            xssmain(url)  # protocol

        elif command == '--chu':
            f = open("url.txt", "w")
            newurl = input("New URL: ")
            f.write(newurl)
            f.close()
            getipfromhost("url.txt")
            genDir()
            print("------------------------------")

    elif command in closelist:
        print("Close program")
        global state
        state = False
        return
    else:
        print('+++ Command no found +++\n')


if __name__ == "__main__":
    print("\n----- SECURITY ASSESSMENT TOOLSUSING OWASP GUIDELINE -----")
    while state:
        program()

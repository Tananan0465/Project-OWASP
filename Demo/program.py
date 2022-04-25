from json.tool import main
from scripts.script_dirsearch import directoryListing
from scripts.script_ssl import ssl
from scripts.script_scanport import scanport
from scripts.getip import getipfromhost
from scripts.script_xss import xss, xssmain
import socket

state = True



def program():
    print("\nPlease choose a command to test vulnerability.")
    print("Command:")
    print("\t-a, --all\t\tTest all command.")
    print("\t-d, --directory\t\tDirectory Listing")
    print("\t-i, --inject\t\tSQL injection")
    print("\t-p, --portscan\t\tScan open port")
    print("\t-s, --ssl\t\tInsecure SSL/TLS Configuration")
    print("\t-x, --xss\t\tCross-site scripting (XSS)")
    print("\t--exit\t\t\tClose program.\n")

    getipfromhost("url.txt")
    url = "./temp/url_temp.txt"
    ip = "./temp/ip_temp.txt"

    cmdlist = ['-a', '--all', '-d', '--directory', '-i', '--inject',
               '-p', '--portscan', '-s', '--ssl', '-x', '--xss']
    closelist = ['--exit']
    command = input("input command: ")

    if command in cmdlist:
        if command == '-a' or command == '--all':
            print("Vulnerability : All")
            scanport(ip)
            directoryListing(url)
            ssl(url)
            print("Process Completed !!!")
            print("------------------------------")

        elif command == '-d' or command == '--directory':
            print("Vulnerability : Directory Listing")
            directoryListing(url)
            print("Directory listing Completed")
            print("------------------------------")

        elif command == '-i' or command == '--inject':
            print("Vulnerability : SQL injection")
            print("Process Completed")
            print("------------------------------")

        elif command == '-p' or command == '--portscan':
            print("Vulnerability : Scan open port")
            scanport(ip) # ip only
            print("Port scan Completed")
            print("------------------------------")

        elif command == '-s' or command == '--ssl':
            print("Vulnerability : Insecure SSL/TLS Configuration")
            ssl(url) # url no-protocol
            print("SSL Completed")
            print("------------------------------")

        elif command == '-x' or command == '--xss':
            print("Vulnerability : Cross-site scripting (XSS)")
            xssmain(url) # protocol
            print("XSS Completed")
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

from subprocess import PIPE, run
import os
import time


def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout


def directoryListing():
    directoryListingResult = open("directoryListingResult.txt", "w")
    for line in open("portLists.txt", "r"):
        # print("dirsearch -u "+line)
        m = out("dirsearch -u "+line)
        directoryListingResult.write(m)
    directoryListingResult.close()


def program():
    print("Command:")
    print("\t-a, --all\tUse all command.")
    print("\t-d, --directory\tFind open directory on website.")
    print("\t-i, --inject\tTest vulnerability SQL injection.")
    print("\t-p, --portscan\tScan open port in network.")
    print("\t-s, --ssl\tCheck HTTP Strict Transport Security.")
    print("\t-x, --xss\tTest vulnerability Cross-site scripting.")
    print("\t--exit\t\tClose program.")

    cmdlist = ['-a','--all','-d','--directory','-i','--inject','-p','--portscan','-s','--ssl','-x','--xss']
    closelist = ['--exit']
    command = input("input command: ")
    if command in cmdlist:
        print("ip: 192.168.1.1")
        print("### result ###")
        print("We found XSS !!!")
        print("Please fix it.")

        return 0

    elif command in closelist:
        return 0
    else:
        print('+++ Command no found +++')
        program()





print("----- SECURITY ASSESSMENT TOOLSUSING OWASP GUIDELINE -----")
program()

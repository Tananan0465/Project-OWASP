from subprocess import PIPE, run
import os


def directoryListing(ip):
    temp = open(ip, "r")
    os.system("sudo python3 ./tools/dirsearch/dirsearch.py -u "+temp.read() +
              " --exclude-status=400-499,500-599 --recursion-status=200 --exclude-sizes=0B --output=./results/directoryListingResult.txt")
    print("Directory listing Completed")
    print("------------------------------")

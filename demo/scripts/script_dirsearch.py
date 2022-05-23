from subprocess import PIPE, run
import os
from scripts.genDir import genDirName


def directoryListing(ip):
    temp = open(ip, "r")
    dirname = open("./temp/url_temp.txt", "r").read()
    os.system(f"sudo python3 ./tools/dirsearch/dirsearch.py -u {temp.read()} --exclude-status=400-499,500-599 --recursion-status=200 --exclude-sizes=0B --output=./results/{genDirName(dirname)}/directoryListingResult.txt")
    print("Directory listing Completed")
    print("------------------------------")

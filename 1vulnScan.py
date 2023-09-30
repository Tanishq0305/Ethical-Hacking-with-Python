import socket
import os
import sys

#add vulnbanners.txt file in the folder
def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except:
        return
    
def checkVulns(banner, filename):
    f = open(filename, "r") #opening and reading file in python
    for line in f.readlines():
        if line.strip("\n") in banner:
            print("[+] Server is vulnerable: "+ banner.strip("\n"))

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print("[-] File doesn't exit!!!")
            exit(0)
        if not os.access(filename, os.R_OK):
            print("[-] Access denied")
            exit(0)
    else:
        print("[-] Usage: "+ str(sys.argv[0])+ " <vuln filename>") 
        exit(0)
    portlist = [21,22,25,80,110,443,445]
    for x in range(4,6):
        ip = "IP_Address"+str(x) #add ip address
        for port in portlist:
            banner = retBanner(ip,port)
            if banner:
                print("[+] "+ip+"/"+str(port)+" : "+banner)
                checkVulns(banner, filename)

main()
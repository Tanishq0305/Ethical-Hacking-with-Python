#cracking sha1 password from online passlist
from urllib.request import urlopen 
from termcolor import colored
#this will be only funct we using from this library
import hashlib

sha1hash = input("Enter sha1 hash: ")

passlist = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000.txt').read(), 'utf-8')

for password in passlist.split('\n'):
    hashguess = hashlib.sha1(bytes(password, 'utf-8')).hexdigest()
    if hashguess == sha1hash:
        print(colored("[+] The password is: "+str(password),'green'))
        quit()
    else:
        print(colored("[-] Password guess "+str(password)+" does not match, trying next...",'red'))
      
from termcolor import colored
import hashlib

def tryopen(wordlist):
    global pass_file
    try:
        pass_file = open(wordlist, 'r')
    except:
        print("[!!] No such file at the path")
        quit()

pass_hash = input("[*] Enter MD5 hash value: ")
wordlist = input("[*] Enter path to the password file: ")

tryopen(wordlist)

for word in pass_file:
    print(colored("[-] Trying: "+word.strip("\n"), 'red' ))
    enc_wrd = word.encoder('utf-8')
    md5digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    if md5digest == pass_hash:
        print(colored("[+] Password found: "+word, 'green'))
        exit(0)
print("[-] Password not in list")
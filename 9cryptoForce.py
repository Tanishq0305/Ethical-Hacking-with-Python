from termcolor import colored
import crypt

def crackPass(cryptword):
    salt = cryptword[0:2]
    dictionary = open("dictionary.txt", 'r')
    for word in dictionary.readlines():
        word= word.strip('\n')
        cryptPass = crypt.crypt(word, salt)
        if (cryptword == cryptPass):
            print(colored("[+] Found Password: "+word, 'green'))
            return True
            

def main():
    passFile = open('pass.txt','r')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptWord = line.split(':')[1].strip(' ').strip('\n')
            print(colored("[*] Cracking Password for: "+user, 'yellow'))
            crackPass(cryptWord)
   

    main()
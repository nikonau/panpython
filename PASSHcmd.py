#
# Log into PAN Firewall via SSH and restart DNS Proxy
# which is causing mgmt cpu spike on PAN OS 9.0.3
# Requires Python 2.x
# This version allows you to input hostname, username, password and cmd from stdin.
# Setup crontab schedule to automatically execute
#

import paramiko
import time

#HOSTNAME = '10.10.10.1'  #Firewalls IP
PORT = 22 

def ssh_command(username, password, cmd, hostname, port=PORT):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.load_system_host_keys()
    ssh_client.connect(hostname, port, username, password)
    remote_conn = ssh_client.invoke_shell()
    print "Interactive SSH session established"
    remote_conn.send("set cli pager off\n")
    remote_conn.send(""+cmd+"\n")
    time.sleep(8)
    buff = ''
    while not buff.endswith('>'):
        resp = remote_conn.recv(15000)
        buff += resp
        print(resp)

if __name__ == '__main__':
    hostname = input("Enter hostname or IP address:")
    username = input("Enter username: ")
    password = input("Enter password: ")  
    cmd = input("Enter command:")
    ssh_command(username, password, cmd)

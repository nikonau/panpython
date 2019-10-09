#
# Log into PAN Firewall via SSH and restart DNS Proxy which is causing mgmt cpu spike on PAN OS 9.0.3
# Requires Python 2.x
# Setup crontab schedule to automatically execute
#
import paramiko
import time

USERNAME = 'username'
PASSWORD = 'password'
HOSTNAME = '192.168.0.1'  #Firewalls IP
PORT = 22

def ssh_command(username=USERNAME, password=PASSWORD, hostname=HOSTNAME, port=PORT):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.load_system_host_keys()
    ssh_client.connect(hostname, port, username, password)
    remote_conn = ssh_client.invoke_shell()
    #print ("Interactive SSH session established")
    remote_conn.send("debug software restart process dnsproxy\n ")
    time.sleep(8)
    remote_conn.send("exit\n ")


if __name__ == '__main__':
    ssh_command()

#
#Log into PAN Firewall via SSH and restart DNS Proxy which is causing mgmt cpu spike on PAN OS 9.0.3
#
import paramiko
import time

USERNAME = 'username'
PASSWORD = 'password'
HOSTNAME = '192.168.1.1'  #Firewalls IP
PORT = 22

def ssh_command(cmd, username=USERNAME, password=PASSWORD, hostname=HOSTNAME, port=PORT):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.load_system_host_keys()
    ssh_client.connect(hostname, port, username, password)
    remote_conn = ssh_client.invoke_shell()
    print ("Interactive SSH session established")
    remote_conn.send(""+cmd+"\n")
    time.sleep(8)
    buff = ''
    while not buff.endswith('>'):
        resp = remote_conn.recv(15000)
        buff += resp
        print(resp)

if __name__ == '__main__':
    cmd = 'debug software restart process dnsproxy'
    ssh_command(cmd)
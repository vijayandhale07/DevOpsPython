# Important Python Libraries for DevOps

# subprocess - run shell commands

import subprocess
subprocess.run(["ls","-l"])


# paramiko - SSH automation

import paramiko 

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("server_ip",username="user",passwrod="pass")



stdin, stdout, stderr = ssh.exec_command("uptime")
print(stdout.read().decode())

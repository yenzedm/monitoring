#!C:\Users\admin\AppData\Local\Programs\Python\Python39\python.exe
import subprocess
import re


result = subprocess.run(['C:\\RECFACES\\AUX_APP\\SRV\\erl\\lib\\rabbitmq_server-3.9.5\\sbin\\rabbitmqctl.bat', 'status'], capture_output=True, text=True)

stdout = result.stdout
stdeer = result.stderr

if stdeer:
    print(stdeer)
    exit(1)

pattern = r'Connection count.*'
tmp = re.search(pattern=pattern, string=stdout)

conn = int(tmp.group(0).split()[2])
print(conn)
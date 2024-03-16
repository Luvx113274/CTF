from pwn import *

nc = remote('83.136.254.223', 46312)

nc.sendline(b'y')
a = nc.recv(1024).decode('utf-8').split('\n')[-2]

b = a.split(', ')
s = ""
for i in b:
    if i == 'GORGE':
        s += "STOP-"
    elif i == 'FIRE':
        s += "ROLL-"
    elif i == 'PHREAK':
        s += "DROP-"
nc.sendline(s[:-1].encode())

while True:
    a = nc.recv(1024).decode('utf-8')
    print(a)
    b = a.split('\n')[0].split(', ')
    s = ""
    for i in b:
        if i == 'GORGE':
            s += "STOP-"
        elif i == 'FIRE':
            s += "ROLL-"
        elif i == 'PHREAK':
            s += "DROP-"
    nc.sendline(s[:-1].encode())
    sleep(0.5)

# Flag is: HTB{3v4l_0r_3vuln??}
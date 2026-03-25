from pwn import *


class GlibcRand:
    DEG = 31
    SEP = 3
    MASK = 0xffffffff

    def __init__(self, seed):
        self.state = [0]*self.DEG
        self.state[0] = seed & 0x7fffffff

        # inizializzazione Park–Miller
        for i in range(1, self.DEG):
            self.state[i] = (16807 * self.state[i-1]) % 2147483647

        self.fptr = self.SEP
        self.rptr = 0

        # warm-up ESATTO
        for _ in range(10 * self.DEG):
            self.rand()

    def rand(self):
        val = (self.state[self.fptr] + self.state[self.rptr]) & self.MASK
        self.state[self.fptr] = val

        self.fptr = (self.fptr + 1) % self.DEG
        self.rptr = (self.rptr + 1) % self.DEG

        return (val >> 1) & 0x7fffffff

r=GlibcRand(1)
v2 = r.rand() % 16 + 5
v3=bytearray(v2)
for i in range(v2):
    v3[i] = r.rand() % 42 + 48
re=remote("flagvault.challs.olicyber.it", 34000)
re.sendline(v3)
re.recvline()
print(re.recvline(drop=True).decode())
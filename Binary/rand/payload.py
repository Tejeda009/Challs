class GlibcRand:
    DEG = 31
    SEP = 3
    MASK = 0xffffffff

    def init(self, seed):
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
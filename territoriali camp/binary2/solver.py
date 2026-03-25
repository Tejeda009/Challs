
i_1=36
enc=bytearray.fromhex("756b292e21df7d4cbdbbcb6e41305d9985b3b36e43a258929d1b935aa79aadc8855bb751")
def reverse_bytes(enc,i):
    return enc[::-1]
def rol8(a1, a2):
  return (a1 << (a2 & 7)) | (a1 >> (-(a2 & 7) & 7)) & 0xFF
def ror8(a1, a2):
    return (a1 >> (a2 & 7)) | (a1 << (-(a2 & 7) & 7)) & 0xFF
enc = reverse_bytes(enc, i_1)
for i in reversed(range(i_1)):
    enc[i] -= i
for i in reversed(range(i_1)):
    enc[i] = ror8(enc[i], i&7)
for i in reversed(range(i_1)):
    enc[i] ^= 0x37
print(enc)


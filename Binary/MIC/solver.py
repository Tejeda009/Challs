flagx=bytearray.fromhex("313f2f3233565064256c2c477425075e6a2b6e37262c56")
secret=bytearray.fromhex("313f2f3233565064256c2c477425075e6a2b6e37262c56")
for i in range(len(flagx)):
   flagx[i]^=secret[i]
print(flagx)
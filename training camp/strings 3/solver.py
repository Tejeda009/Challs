flag=bytearray.fromhex("D45CDCBB6B1ED34A4A5ED2DFAC7C0000")
key =bytes.fromhex("B230BDDC107AE17B2C3BE2EC9901")
for i in range(14):
    flag[i]=flag[i]^key[i]
print(flag)
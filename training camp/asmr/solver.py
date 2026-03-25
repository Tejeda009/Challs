data1=bytearray.fromhex("BDC3B5ACD5D9CDDBB5B7C9E8B5BD81C7D689C4DBBC77DDD4")
data2=bytearray.fromhex("575754455A66586842425776545050686A55657550437657")
flag=bytearray()
for i in range(len(data1)):
    flag.append(data1[i]-data2[i])
print(flag)
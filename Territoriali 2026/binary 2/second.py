flagx=bytearray("51}40yw{gu_yltcr0ud_h1a9gf_fnhr67cf_","utf-8")
maph=bytearray.fromhex("20 07 24 11 17 12 10 05  19 0D 13 0B 02 14 22 0E 0C 18 09 0A 1A 23 03 1F  04 01 0F 21 08 15 16 1C 1D 1E 06 1B")
mapb=bytearray.fromhex("1F 06 23 10 16 11 0F 04  18 0C 12 0A 01 13 21 0D 0B 17 08 09 19 22 02 1E  03 00 0E 20 07 14 15 1B 1C 1D 05 1A")
flag=''
cont=0

for i in range(len(maph)):
    cont=0

    for j in range(len(maph)):

        if(maph[j]==(i+1)):
            break
        else:
            cont+=1
    print(chr(flagx[cont]),end="")
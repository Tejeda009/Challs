v3 = {}
v3[0] = 13
v3[1] = 25
v3[2] = 31
v3[3] = 10
v3[4] = 11
v3[5] = 15
v3[6] = 44
v3[7] = 51
v3[8] = 4
v3[9] = 46
v3[10] = 19
v3[11] = 28
v3[12] = 22
v3[13] = 50
v3[14] = 9
v3[15] = 30
v3[16] = 18
v3[17] = 20
v3[18] = 0
v3[19] = 26
v3[20] = 45
v3[21] = 42
v3[22] = 6
v3[23] = 48
v3[24] = 2
v3[25] = 39
v3[26] = 16
v3[27] = 7
v3[28] = 8
v3[29] = 24
v3[30] = 34
v3[31] = 17
v3[32] = 37
v3[33] = 36
v3[34] = 14
v3[35] = 3
v3[36] = 41
v3[37] = 33
v3[38] = 12
v3[39] = 23
v3[40] = 1
v3[41] = 40
v3[42] = 35
v3[43] = 49
v3[44] = 27
v3[45] = 21
v3[46] = 29
v3[47] = 43
v3[48] = 32
v3[49] = 47
v3[50] = 5
v3[51] = 38
#per reversare la cosa sopra possiamo a fare una nuova variabile result, andare a iterare fino a < 0x34
#e fare result[v3[i]] = byte[i] in cui v3[i] corrisponde alla posizione originale e byte[i] corrisponde al carattere che dovrebbe trovarsi in v3[i] e invece si trova a i
#4) dopo aver ordinato fa lo xor con sta roba
xorkey = bytes.fromhex("9af81f2b1be0ab1fc362fedaa83f703c751930a048c154ca75e675a6de166eef18ede6fce41106a3af5e1d24f65dca8ea3ea96a5")
#5) infine fa un controllo per assicurarsi che il risultato sia uguale a s1. qui ci potrebbe essere della confusione ma praticamente
# strcmp da 0 se e' uguale e 1 se non e' uguale quindi la funzione sbagliata viene chiamata in modo logico
#s1 corrisponde a questo:
s1 = bytes.fromhex("AA A7 7D 74 69 81 92 62 B8 07 CF A8 9C 07 11 63 17 77 56 D8 79 F1 21 AC 14 82 2A 96 AA 73 59 9C 29 DA 92 9B D0 70 73 FC C3 3F 78 40 C6 33 FE EF 95 DE E4 C7")
#iniziamo da fare lo xor con xorkey
result = bytearray(0x34) #il corrispondente della variabile byte dello step 3
for i in range(0x34):
    result[i] = s1[i]^xorkey[i]
#adesso facciamo quanto introdotto nello step 3. dobbiamo pero' dichiararci un'altra variabile
result2 = bytearray(0x34)
for i in range(0x34):
    result2[v3[i]] = result[i]
print(result2.decode())
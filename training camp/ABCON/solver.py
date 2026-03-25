from string import ascii_letters

input="BBABA BABAB BBBBB BBAAB { ABABB BBAAA BBABB ABBBB BBABB _ BBBBB ABBBB BBABB _ BABAA ABAAB _ BBABB BBAAB BBAAB ABBBA }"
input=input.split(" ")
dict=[]
for i in range(len(input)):
    if(input[i]!='{') and (input[i]!='}') and (input[i]!='_'):
        input[i]=input[i].replace("A","1").replace("B","0")#sostituisco le lettere con 0 e 1
        input[i]=int(input[i],2)#converto le stringhe binarie in numeri interi
for i in range(len(ascii_letters))[:-1]:
    dict.append((i, ascii_letters[i]))#creo un dizionario con le lettere e i loro indici
for i in range(len(input)):
    if(input[i]!='{') and (input[i]!='}') and (input[i]!='_'):
        print(input[i])
        print(dict)
        input[i]=dict[input[i]][1]#sostituisco i numeri con le lettere corrispondenti
input="".join(input)#unisco le lettere in una stringa
print(input)
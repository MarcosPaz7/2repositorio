print("digite uma frase : ")
frase=input()
fra2=""
marcador=" "

for n in frase:
    if marcador ==" ":
        fra2=fra2+n.upper()
        marcador=1
    else:
        fra2=fra2+n.lower()
        marcador=" "
        
print(fra2)    
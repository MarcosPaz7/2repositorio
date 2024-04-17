print('digite uma frase :')
frase=str(input())
VOGAIS=["a","e","i","o","u"]
print(len(frase))

contador=0
#conto as vogais 
for n in frase:
    if n in VOGAIS:
        contador=contador+1
print("numero de vogais é: "+str(contador))

frase=frase.replace(" ","")
print("numero de consoante é "+str(len(frase)-contador))



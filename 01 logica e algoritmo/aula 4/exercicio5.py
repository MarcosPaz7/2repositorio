print("digite uma frase ou palavra" )
frase=input().lower().replace(" ","")
print(frase)
decremento=int(len(frase))-1
resultado="é polindromo"

print(decremento)

for n in frase:
    print(n)
    teste=frase[decremento]
    if n != teste:
        resultado=" nao é polindromo "
    decremento-=1    

print(resultado)    
print("digite um numero e tenha seu fatorial ")
numero=int(input())
fatorial=numero*(numero-1)
numero=numero-2


while numero >=1:
    fatorial=fatorial*(numero)
    numero-=1
    

print(fatorial)

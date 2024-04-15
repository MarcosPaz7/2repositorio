print("informe um numero para taboada")
numero=int(input()) 

for indice in range(1,11):
    print(str(numero)+" * "+str(indice)+" = "+str(numero*indice))
    
print("Digite seu peso")
peso=float(input())

print("digite sua altura")
altu=float(input())
imc=peso/(altu*altu)

if imc>40:
    print("VOCA ESTA COM OBESIDADE 3 MORBIDA seu imc é "+str(imc))
elif imc>=35:
    print("obesidade grau 2 (severa ) seu imc é "+str(imc))
elif imc>=30:
    print("obesidade grau 1 seu imc é "+str(imc))
elif imc>=25:
    print("levemente acima do peso seu imc é "+str(imc))
elif imc>=18.6:
    print("peso ideal seu imc é "+str(imc))
else:
    print("abaixo do peso seu imc é "+str(imc))    

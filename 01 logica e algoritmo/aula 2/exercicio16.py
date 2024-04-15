print("digite um valor :")
valor=float(input())
print("A - para Real para Dolar")
print("B - para Dolar para Real")
print("C - para Real para Euro")
print("D - para Euro para Real")
opcao=input()

if opcao=="A":
    print("o valor em dolares é : "+str(valor/5.5))

elif opcao=="B":
    print("o valor em Reais é : "+str(valor*5.5))

elif opcao=="C":
    print("ovalor em euro é : "+str(valor/4.75))

elif opcao=="D":
    print("ovalor em reais é : "+str(valor*4.75))

else:
    print("nenhuma das opções foi celecionada")     

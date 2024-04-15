print('informe um numero1  inteiro')
nu1=int(input())

print('informe um numero2  inteiro')
nu2=int(input())

print('informe um numero3  inteiro')
nu3=int(input())

if nu1<nu2 and nu1<nu3:
    print('numero 1 e menor numero '+str(nu1))
elif nu2<nu1 and nu2<nu3:
    print("numero 2 e o menor "+str(nu2))
else:
    print("numero  3 e o menor "+str(nu3))
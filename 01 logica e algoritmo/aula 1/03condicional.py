#condicional simples 
idade=18

if idade>=18:
    print("pode obter CNH")
else:
    print("Não pode obter CNH")

# condicional

media = 7
if media == 10:
    print("nota maxina parabens")
elif media >= 9: 
    print("otimo")
elif media >= 8:
    print("bom ")
elif media >= 7:
    print("na media ")
elif media >= 5:
    print(" em exame")
else:
    print("reprovado")

#operadores logicos

valor=-100.5
if valor >=0 and valor<=100:
    print("valor esta enter 0 e 100 valor é : "+str(valor))
else:
    print('valor nao esta entre 0 e 100 valor é '+str(valor))

total=85
fpagamento="avista"

if total >=100 and fpagamento=="avista":
    print("total a pagar : R$"+str(total*0.9))
else:
    print("total a pagar : R$"+str(total))


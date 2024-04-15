print("informe o valor da compra ")
valor=float(input())

print("informe a forma de pag avista ou prazo ")
ForPagamento=str(input())

if valor>=500 and ForPagamento=="avista":
    print("valor a ser pago é "+str(valor-valor*0.15))
else :
    print("valor a ser pago é ."+str(valor))








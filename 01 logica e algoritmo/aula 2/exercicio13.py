print("informe o primeiro numero :")
num1=int(input())

print("informe o segundo numero ")
num2=int(input())

print("informe o terceiro Numero ")
num3=int(input())

if num1<num2 and num1<num3:
    if num2<num3:
        print(str(num1)+" "+str(num2)+" "+str(num3))
    else:
        print(str(num1)+" "+str(num3)+" "+str(num2))

elif num2<num1 and num2<num3:
    if num1<num3:
        print(str(num2)+" "+str(num1)+" "+str(num3))
    else:
        print(str(num2)+" "+str(num3)+" "+str(num1))
else:
    if num1<num2:
        print(str(num3)+" "+str(num1)+" "+str(num2))        
    else:
        print(str(num3)+" "+str(num2)+" "+str(num1))    


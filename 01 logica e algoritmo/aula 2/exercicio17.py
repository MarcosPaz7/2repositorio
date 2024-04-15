print("digite  a temperatura em ")
temp=float(input())

print("digite A para traformar celsios em fahrenheit")
print("digite B para traformar fahrenheit em Calsios")
opcao=input()

if opcao=="A":
    print("A temperatura em fahrenheit é "+str(temp*1.8+32))
elif  opcao=="B" :
    print ("A Temperarura em Celsios é "+ str((temp-32)/1.8))
else:
    print("nenhuma  opção digitada")    
          
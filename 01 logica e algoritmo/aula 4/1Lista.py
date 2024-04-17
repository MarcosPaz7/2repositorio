nomes=['marcos','ana',"Arthur","Antonio"]
for n in nomes:
    print(n)
print('--------------------------------------') 
# adicionar um novo nome append
nomes.append("jhony")   
indice=0
while indice<len(nomes):
    print(nomes[indice])
    indice+=1

print('--------------------------------------') 
# alterar um nome
nomes[1] ="troca" 
indice=0
while indice<len(nomes):
    print(nomes[indice])
    indice+=1

print('--------------------------------------') 
# remover ex nomes.remove("troca") ou no nomes.pop(1)
nomes.pop(1)
indice=0
while indice<len(nomes):
    print(nomes[indice])
    indice+=1

 


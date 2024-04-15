nome=""
lista=[]

while nome.lower()!="sair":
    print("informe um nome ou sair :")
    nome=input()

    if nome.lower()!="sair":
        lista.append(nome)
print("-------------------------------------------")

for n in lista:
    print(n)    
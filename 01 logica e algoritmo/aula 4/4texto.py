#variavel contendo uma frase
frase='aprendendo manipular texto com python'

#contar os  caranteres 
print("a quantidade de caracteres é "+str(len(frase)))
print('------------------------------------------')

#obter caracteres individualmente 
for f in frase:
    print(f)

print('------------------------------------------')    

#Passar a primeira letra pra maiuscula 
print(frase.capitalize())
print('------------------------------------------') 

#deixar tudo em maiusculo 
print(frase.upper())
print('------------------------------------------')

#deixar tudo em minusculo 
print(frase.lower())
print('------------------------------------------')

#alterar termos 
print(frase.replace(" ",""))
print(frase.replace(" ","-"))
print('------------------------------------------')

#covertendo testo em vetor 
vetor =frase.split(' ')
print("tamanho do vetor é "+str(len(vetor)))

#impromir uma  letra da palavra / testo  comforme sua posição 
frase = "teste"
print(frase[0])





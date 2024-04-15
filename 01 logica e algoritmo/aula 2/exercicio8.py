print("digite a nota 1")
nota1=float(input())

print("digite a nota 2")
nota2=float(input())

print("digite a nota 3")
nota3=float(input())

media=(nota1+nota2+nota3)/3

if media >=7 :
    print("voce foi Aprovado sua media é :"+str(media))
elif media>=5 :
    print("voce em exame sua media é :"+str(media))
else:
    print("voce em foi reprovado :"+str(media))


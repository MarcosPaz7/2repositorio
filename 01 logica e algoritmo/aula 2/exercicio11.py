print("digite o valor do 1 lado do triandulo ")
lad1=int(input())

print("digite o valor do 2 lado do triandulo ")
lad2=int(input())

print("digite o valor do 3 lado do triandulo ")
lad3=int(input())

if lad1==lad2 and lad2==lad3 :
    print('Triangulo equilatero')
elif lad2 != lad1 and lad2!=lad3 and lad3!=lad1:
    print("TRIANGULO ESCALENO")
else:
    print("Isoceles")
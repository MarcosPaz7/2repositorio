print("digite que horas sao em brasilia: ")
horas=int(input())

print("digite um numero referenta a cisade para saber as horas 1-Nova York  2-Toquio 3-Lisboa")
cidade=int(input())

if cidade==1:
    hc=horas-2
    if hc<0:
        hc=24-hc
        print("em Nova york são "+str(hc))
    else:
        print("em Nova york são "+str(hc))

elif cidade==2:
    hc=horas+12
    if hc>24:
        hc=hc-24
        print("em Toquio sao :"+str(hc))
    else:
        print("en toquio sao : "+str(hc))  
else:
    hc=horas+3
    if hc>24:
        hc=hc-24
        print("em Lisboa sao "+str(hc))                 
    else:
        print("em lisboa sao "+str(hc))    

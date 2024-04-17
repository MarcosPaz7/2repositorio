import datetime
#print(datetime.datetime.now())

#exibir apenas data(dia mes ano)
dataformatada=datetime.datetime.now()
hora=int(dataformatada.strftime("%H"))
print(hora)
if hora>=0 and hora<=5:
    print("boa madrugada")
elif hora>=6 and hora<=11:
    print("boa dia ")
elif hora>=12 and hora<=17:
    print("boa Tarde")
elif hora>=18 and hora<=23:
    print("boa Noite")        




#print(dataformatada.strftime('%d-%m-%Y %H:%M '))
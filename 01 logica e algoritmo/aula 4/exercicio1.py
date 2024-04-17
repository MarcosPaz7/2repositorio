#importar  pacote de tempo (data -hora)
import datetime
#print(datetime.datetime.now())

#exibir apenas data(dia mes ano)
dataformatada=datetime.datetime.now()
print(dataformatada.strftime('%d-%m-%Y %H:%M '))
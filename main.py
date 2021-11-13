import datetime

data = datetime.date(2021, 11, 12)

#normal
#print (data)

#formatado
#print(data.ctime())

#acessando informação de data
dia = data.day
mes = data.month
ano = data.year

#print (dia, mes, ano)

#alterando uma informação de data
#nota_data = data.replace(month=10)
#print (data)
#print (nota_data)

#pegando dia de hoje
hoje = datetime.date.today()
#print (hoje)

#fazendo operações com data
delta = hoje - data 
#print (delta) #quantidade de dias entre hoje e a data

data_futuro = hoje+delta
#print(data_futuro)


#hora
hora = datetime.time(12,45,23)
#print(hora)

#print(hora.hour)
#print(hora.minute)
#print(hora.second)

#hora atual
hora_atual = datetime.datetime.now()
#print(hora_atual)

#data e hora atual em string
data_string = hora_atual.strftime("%m/%d/%Y %H:%M:%S")
#print(data_string)

#aplicação - registro de logs
comentarios = []

comentario = None

while comentario!= '':
    comentario = input('Insira seu comentario: ')
    data_public = datetime.datetime.now()
    data_public_str = data_public.strftime("%m/%d/%Y %H:%M:%S")
    comentarios.append((comentario,data_public_str))

for comentario in comentarios[:-1]:
    print(comentario)

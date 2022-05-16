cidade = str(input('Digite o nome da sua cidade: ')).strip()
cidade = cidade.split()
print('Santo'in cidade)
print(cidade[0].upper() == 'SANTO')

cidade = str(input('Digite a sua cidade: ')).upper().split()
print('SANTO' == cidade[0])

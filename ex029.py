velocidade = int(input('Qual a sua velocidade? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print(f'MULTADO! Você excedeu o limite permitido que é de 80km/h. Você deve pagar uma multa de R${multa}.')
print('Tenha um bom dia! Dirija com segurança!')

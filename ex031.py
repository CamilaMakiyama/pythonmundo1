distancia = float(input('Qual a distância da viagem? '))
if distancia >= 200:
    promocional = distancia * 0.45
    print(f'O valor da passagem acima de 200km é: R${promocional}')
else:
    total = distancia * 0.50
    print(f'O valor da passagem até 200km é: R${total}')
preco = distancia * 0.45 if distancia >= 200 else distancia * 0.50
print(f'O valor da sua passagem é: R${preco}')
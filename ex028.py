from random import randint
adivinhe = int(input('Qual número eu pensei? '))
random = randint(0,5)
print('Processando...')
if random == adivinhe:
    print('Parabéns, você acertou!')
else:
    print('Não foi dessa vez, tente novamente!')
    print(f'Eu pensei no número: {random}')

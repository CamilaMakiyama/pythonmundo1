a = str(input('Digite o primeiro nome: '))
b = str(input('Digite o segundo nome: '))
c = str(input('Digite o terceiro nome: '))
d = str(input('Digite o quarto nome: '))
import random
lista = [a, b, c, d]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}.')

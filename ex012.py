preco = float(input('Digite o valor do produto: '))
porcentagem = preco * 0.05
desconto = preco - porcentagem
print(f'O valor do produto é RS{preco}, com o desconto de 5% aplicado o valor passa a ser RS{desconto:.2f}.')

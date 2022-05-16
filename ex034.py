salario = float(input('Digite o valor do funcionário: R$'))
if salario > 1250:
    aumento = salario + (salario*0.10)
    print(f'O seu salário com aumento é: R${aumento}')
else:
    aumento = salario + (salario*0.15)
    print(f'Seu salário com aumento é: R${aumento}')

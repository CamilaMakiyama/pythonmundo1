frase = str(input('Digite uma frase: ')).lower()
print(f'Quantas vezes a letra (a) aparece: {frase.count("a")}')
print(f'A posição do primeiro (a) é: {frase.find("a")} ')
print(f'A posição da ultima vez que o (a) aparece: {frase.rfind("a")}')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1+n2
print('A soma vale:', s)
print('A soma vale: {}'.format(s))
#print('A soma entre', n1, 'e', n2, 'é:',s)
print('A soma entre {} e {} vale: {}'.format(n1, n2, s))
print(f'A soma entre {n1} e {n2} vale: {s}')
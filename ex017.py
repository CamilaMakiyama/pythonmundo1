import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjascente: '))
s = (co ** 2 + ca ** 2)
hi = math.sqrt(s)
print(f"O valor da hipotenusa é {hi:.2f}.")
hi2 = math.hypot(co, ca)
print(f'O valor da hipotenusa é {hi2:.2f}.')

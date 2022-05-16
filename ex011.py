largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
tinta = area / 2
print(f'A largura da parede  é {largura}m e a altura é {altura}m, logo a área mede {area}m².\nPara essa área é '
      f'necessário usar {tinta:.2f}l de tinta.')

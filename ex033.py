primeiro = int(input('Digite o primeiro valor: '))
segundo = int(input('Digite o segundo valor: '))
terceiro = int(input('Digite o terceiro valor: '))
if primeiro<segundo and primeiro<terceiro:
    print(f'O menor valor foi {primeiro}.')
if segundo<primeiro and segundo<terceiro:
    print(f'O menor valor foi {segundo}.')
if terceiro<primeiro and terceiro<segundo:
    print(f'O menor valor é {terceiro}.')
if primeiro>segundo and primeiro>terceiro:
    print(f'O maior número foi {primeiro}.')
if segundo>primeiro and segundo>terceiro:
    print(f'O maior número foi {segundo}.')
if terceiro>primeiro and terceiro>segundo:
    print(f'O maior número foi {terceiro}.')

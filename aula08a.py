# import math (importa toda a biblioteca de matemática)
# from math import xxxx, yyyy (dessa forma só será importado o que for especificado no campo xxxx e yyyy)
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é igual a {}'.format(num, math.floor(raiz)))

# É possível utilizar bibliotecas disponibilizadas por outros programadores, basta importá-la
import emoji
print(emoji.emojize('Olá, Mundo! :globe_with_meridians:'))

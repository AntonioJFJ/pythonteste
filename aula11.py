print('\033[0;31;43mOlá, Mundo!')
print('\033[1;31;44mOlá, Mundo!\033[m')
print('\033[4;31;42mOlá, Mundo!\033[m')
print('\033[7;30mOlá, Mundo!\033[m')

nome = str(input('Digite um nome: '))
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Muito prazer em te conhecer, {}{}{}.'.format(cores['amarelo'], nome, cores['limpa']))

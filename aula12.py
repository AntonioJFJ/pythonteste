nome = str(input('Qual é o seu nome?\n'))
if nome == 'Antonio':
    print('Que nome bonito!')
elif nome == 'João' or nome == 'José' or nome =='Maria':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Batman Flash Logan':
    print('O cara é brabo mesmo.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, \033[33m{}!'.format(nome))

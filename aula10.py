nome = str(input('Digite seu primeiro nome: '))
upper = nome.upper()
if upper == 'ANTONIO':
    print('Você é o cara!')
else:
    print('Olá')
print('Bom dia, aluno {}.'.format(nome))
print('-'*20)
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
média = (nota1+nota2)/2
if média >=7:
    print('Sua nota foi {:.1f}\nParabéns {}, você foi aprovado!'.format(média, nome))
else:
    print('Sua nota foi {:.1f}\nInfelizmente você foi reprovado, {}.'.format(média, nome))

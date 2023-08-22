#Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento de String,
# Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().

frase = 'Curso em Vídeo Python'
print(frase[3])
print(frase[3:13])
print(frase[3:13:2])
print(frase[:13])
print(frase[13:])
print(frase[::2])
print(frase.count('o'))
print(len(frase))
print('''What would have taken an experienced developer half an hour to write took ChatGPT 40 seconds. 
It worked equally well for classic arcade games Breakout and Asteroids. ''')

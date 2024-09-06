portugues = 'Olá Mundo!'
ingles = 'Hello World'
print(' ')
while True:
    usuario = input(f'Digite 1 para português e 2 para inglês: ')
    if usuario == '1':
        print(portugues)
        break
    elif usuario == '2':
        print(ingles)
        break
    else:
        print(f'O programa só funciona com 1 e 2. Digite novamente')
        print(' ')


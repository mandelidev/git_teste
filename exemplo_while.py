portugues = 'Olá Mundo!'
ingles = 'Hello World!'

while True:
    usuario = input(f'Digite 1 para português e 2 para inglês: ')
    if usuario == '1':
        print(' ')
        print(portugues)
        break
    elif usuario == '2':
        print(' ')
        print(ingles)
        break
    else:
        print(' ')
        print(f'O programa só funciona com 1 e 2. Digite novamente')
        print(' ')


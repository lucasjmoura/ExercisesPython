if __name__ == '__main__':
    N = int(input())
    lista = []
    lista_commands = {'insert':lista.insert,
                  'append': lista.append,
                  'sort': lista.sort,
                  'pop':lista.pop,
                  'reverse':lista.reverse,
                  'remove': lista.remove}
    for x in range(0, N):
       
        comando = input().split(' ')

        if len(comando) > 1:
            if len(comando) > 2:
                lista_commands[comando[0]](int(comando[1]),int(comando[2]))
            else:
                lista_commands[comando[0]](int(comando[1]))
        elif comando[0] == 'print':
            print(lista)
        else:
            lista_commands[comando[0]]()

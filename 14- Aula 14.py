def par(x):
    return x % 2 == 0

def parouimpar(x):
    if par(x):
        return "par"
    else:
        return "impar"

valor = 0
while valor != 'S':
    valor = input('digite um valor ou "S" para sair: ')
    if valor != 'S':
        print(parouimpar(int(valor)))
    else:
        print('fim do programa')

opcao2 = 0
while opcao2 != 2:
    print('## CALCULADORA DE OPERAÇÕES BÁSICAS ##')
    print('1. Soma \n2. Subtração \n3. Multiplicação \n4. Divisão \n5. Potência \n6. Sair')
    print (10*'--')
    print('selecione a opção desejada: ')
    opcao = float(input('opção: '))

    if opcao == 1:
        n1 = float(input('\nDigite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        res = n1+n2
        print('\n')
        print(10*('~~'))
        print(f'Resultado da soma = {res:.2f}')
        print(10*('~~'))
        print('\ndeseja reiniciar o programa? \n1. Sim \n2. Não')
        opcao2 = int(input('opção: '))
        if opcao2 == 2:
            print('saindo...')

    elif opcao == 2:
        n1 = float(input('\nDigite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        res = n1-n2
        print('\n')
        print(10*('~~'))
        print(f'Resultado da subtração = {res:.2f}')
        print(10*('~~'))
        print('\ndeseja reiniciar o programa? \n1. Sim \n2. Não')
        opcao2 = int(input('opção: '))
        if opcao2 == 2:
            print('saindo...')

    elif opcao == 3:
        print(10*('~~'))
        n1 = float(input('\nDigite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        res = n1*n2
        print('\n')
        print(10*('~~'))
        print(f'Resultado da multiplicação = {res:.2f}')
        print(10*('~~'))
        print('\ndeseja reiniciar o programa? \n1. Sim \n2. Não')
        opcao2 = int(input('opção: '))
        if opcao2 == 2:
            print('saindo...')

    elif opcao == 4:
        print(10*('~~'))
        n1 = float(input('\nDigite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        res = n1/n2
        resto = n1%n2
        print('\n')
        print(10*('~~'))
        print(f'Resultado da divisão = {res:.2f} \nResto da divisão = {resto:.2f}')
        print(10*('~~'))
        print('\ndeseja reiniciar o programa? \n1. Sim \n2. Não')
        opcao2 = int(input('opção: '))
        if opcao2 == 2:
            print('saindo...')

    elif opcao == 5:
        n1 = float(input('\nDigite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        res = n1**n2
        print('\n')
        print(10*('~~'))
        print(f'Resultado da potenciação  = {res:.2f}')
        print(10*('~~'))
        print('\ndeseja reiniciar o programa? \n1. Sim \n2. Não')
        opcao2 = int(input('opção: '))
        if opcao2 == 2:
            print('saindo...')

    elif opcao == 6:
        print('\n')
        print(10*('~~'))
        print('Encerrando programa...')
        print(10*('~~'))
        exit()

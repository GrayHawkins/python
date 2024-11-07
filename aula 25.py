numero = int(input("Digite o seu número: "))
if numero < 2:
    print(f"Número {numero} não é primo!")
elif numero == 2:
    print("Número 2 é primo!")
else:
    for i in range(2, numero):
        if (numero % i) == 0:
            print(f"Número {numero} não é primo!")
            break
        else:
            if i == numero - 1:
                print(f"Número {numero} é primo!")
            else:
                "aqui não será retornado nada"

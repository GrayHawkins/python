# Esse algoritmo verifica se o número que você digitou é primo ou não

número = int(input("Digite o seu número: ")) # recebendo o número

# Retornando o resultado
if número < 2:
    print(f"Número {número} não é primo!")
elif número == 2:
    print("Número 2 é primo!")
else:
    for i in range(2, número):
        if (número % i) == 0:
            print(f"Número {número} não é primo!")
            break
        else:
            if i == número - 1:
                print(f"Número {número} é primo!")
            else:
                "aqui não será retornado nada"

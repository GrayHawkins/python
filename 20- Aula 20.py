total = 0
número = 0
quantidade = 0

def media(total, quantidade):
    return total / quantidade

while True:
    número = float(input("Digite um número diferente de zero para prosseguir: "))
    
    if número != 0:
        total += número
        quantidade += 1
    else:
        print("\nCalculando média...")
        break

if quantidade > 0:
    média = media(total, quantidade)
    print(f"A sua média final é: {média}")
else:
    print("Nenhum número foi digitado")

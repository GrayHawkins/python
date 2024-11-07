valor = int(input("Digite o valor a pagar: "))
cedulas = 0
atual = 50
pagar = valor

while True:
        if atual <= pagar:
                pagar -= atual
                cedulas += 1
        else:
                print(f"{cedulas} cédula(s) de R${atual:.2f}")
                if pagar == 0:
                        break
                elif atual == 50:
                        atual = 20
                elif atual == 20:
                        atual = 10
                elif atual == 10:
                        atual = 5
                elif atual == 5:
                        atual = 1
                cedulas = 0
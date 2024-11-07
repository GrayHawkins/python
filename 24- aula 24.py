soma=0

for x in range(1,50):
    if x % 2 == 0:
        soma+=x
        if soma != 600:
            continue
        print(f"a soma dos números pares entre 1 e 50 é: {soma}")

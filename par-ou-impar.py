def par(x):
    return x % 2 == 0

def parouimpar(x):
    if par(x):
        return "par"
    else:
        return "impar"

print(parouimpar(7))
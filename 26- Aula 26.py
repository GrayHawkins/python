# Esse programa recebe do usuário o registro de 5 alunos com suas notas e retorna todos os registros

Alunos = [] # Lista vazia
Notas = []

# Registrando as informações
for i in range(1,6):
    nome = (input("Digite o nome do aluno: "))
    Alunos.append(nome)
    nota = float(input("Digite a sua nota: "))
    Notas.append(nota)

# Retornando as informações
print("\n----------REGISTRO DOS ALUNOS----------\n")
for i in range(5):
    print(f"{Alunos[i]} = {Notas[i]}")

print("\nFim do código...")

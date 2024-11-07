import time

# Esse código tem como objetivo simular a compra de um ingresso para o cinema com lanches
# O valor do ingresso varia de acordo com quem é e quem não é estudante

# Identificação do cliente
print("~~~~~~~~BANCADA DE INGRESSOS DO CINESYSTEM~~~~~~~~")
nome = input("Digite o seu nome: ")
print("Processando...")

time.sleep(2)

print(f"\nBem vindo(a) {nome}")
time.sleep(2)

# Escolha da sessão
print("\nESCOLHA UMA DAS NOSSAS SESSÕES:\n")
print("1. Robô Selvagem (14:20)")
print("2. Coringa: Delírio a Dois (15:00)")
print("3. Deadpool e Wolverine (15:50)")
print("4. My Hero Academia: Agora é sua vez (16:30)")
print("5. Carlinhos: os 2050 cavalos (17:15)")
print("6. Venom: A Última Rodada (18:00)")
sessão = int(input("\nDigite o número da sua sessão: "))
print("Processando...")
time.sleep(2)

# Apresentação da sessão escolhida
if sessão == 1:
    print("Sessão escolhida: Robô Selvagem (14:20)")
elif sessão == 2:
    print("Sessão escolhida: Coringa: Delírio a Dois (15:00)")
elif sessão == 3:
    print("Sessão escolhida: Deadpool e Wolverine (15:50)")
elif sessão == 4:
    print("Sessão escolhida: My Hero Academia: Agora é sua vez (16:30)")
elif sessão == 5:
    print("Sessão escolhida: Carlinhos: os 2050 cavalos (17:15)")
elif sessão == 6:
    print("Sessão escolhida: Venom: A Última Rodada (18:00)")
print("Processando...")
time.sleep(2)

# menu de lanches
print("\nESCOLHA UM DOS NOSSOS COMBOS:\n")
print("1. Combo Mini (Pipoca pequena + Refri) - R$ 12,00")
print("2. Combo Médio (Pipoca média + Refri) - R$ 16,00")
print("3. Combo Grande (Pipoca grande + Refri) - R$ 20,00")
print("4. Combo Mega (Balde de Pipoca + Refri) - R$ 24,00")
print("5. Combo Delírio (Balde de Pipoca de Coringa: Delírio a Dois + Refri) - R$ 30,00")
print("6. Não quero Lanche")
lanche = int(input("\nDigite a sua opção: "))


# estipulação do preço total dos lanches
if lanche == 1:
    comidas = 12
elif lanche == 2:
    comidas = 16
elif lanche == 3:
    comidas = 20
elif lanche == 4:
    comidas = 24
elif lanche == 5:
    comidas = 30
elif lanche == 6:
    comidas = 0

if lanche < 6:
    quantidade_lanches = int(input("Digite quantos combos desse você irá comprar: "))
elif lanche == 6:
    quantidade_lanches = 0
    print("Entendido")

total_lanches = comidas * quantidade_lanches

time.sleep(1)


# Quantidade de ingressos de estudantes e não estudantes
print("\nPAGUE SEU INGRESSO:\n")
print("Normal = R$ 40,00")
print("Estudantes = R$ 20,00")

ingressos = int(input("\nQuantos ingressos você deseja: "))
estudantes = int(input("Digite a quantidade de estudantes presentes: "))

# Identificação de Estudantes
if estudantes == 0:
    print("Entendido")
elif estudantes > 0:
    input("Digite o código de cada carteira de estudante: ")

# Estipulação do preço total dos ingressos
preço_estudante = 20
preço_normal = 40

total_estudantes = preço_estudante * estudantes
total_normais = preço_normal * (ingressos-estudantes)

print("Processando total...")
time.sleep(2)

# Estipulação do preço total das compras
para_pagar = total_estudantes + total_normais + total_lanches

# Total a ser pago
print(f"\nTotal das compras = R$ {float(para_pagar)}\nDirija-se ao caixa para o pagamento")









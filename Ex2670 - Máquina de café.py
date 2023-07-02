# Ler a quantidade de funcionários em cada cidade
na = int(input())
nb = int(input())
nc = int(input())

# Pré-calcular o gasto para os casos de o refeitório estar nas cidades A, B ou C
gasto_a = 2 * nb + 4 * nc
gasto_b = 2 * na + 2 * nc
gasto_c = 4 * na + 2 * nb

# Encontrar e exibir o menor dentre os três casos
if gasto_a <= gasto_b:
    if gasto_a <= gasto_c:
        print(gasto_a)
    else:
        print(gasto_c)
else:
    if gasto_b <= gasto_c:
        print(gasto_b)
    else:
        print(gasto_c)

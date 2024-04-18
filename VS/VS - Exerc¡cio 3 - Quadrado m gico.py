# Ler dados de entrada
n = int(input())
quadrado = [list(map(int, input().split())) for _ in range(n)]

# Encontrar o zero
for lin in range(n):
    for col in range(n):
        if quadrado[lin][col] == 0:
            lin_zero, col_zero = lin, col

# Calcular somatório completo e incompleto
if lin_zero != 0:
    lin_completa = 0
else:
    lin_completa = 1
soma_esperada = 0
soma_zero = 0
for col in range(n):
    soma_esperada += quadrado[lin_completa][col]
    soma_zero += quadrado[lin_zero][col]

# Mostrar resultado
print(soma_esperada - soma_zero)
print(lin_zero + 1)
print(col_zero + 1)

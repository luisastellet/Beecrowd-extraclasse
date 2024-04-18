# Ler os dados de entrada
n, m = map(int, input().split())
altura = list(map(int, input().split()))

# Para cada haste...
total = 0
for i in range(1, n):
    # ... a quantidade de movimentos pode ser calculada comparando-se a altura desejada com
    # o quanto a haste atual precisaria ser movida juntamente e em relação à anterior para
    # atingir a altura objetivo
    if m >= altura[i - 1]:
        altura[i] += m - altura[i - 1]
    else:
        altura[i] -= altura[i - 1] - m
    total += abs(m - altura[i - 1])

# Ao final, mostrar a quantidade mínima de movimentos
print(total)

# Ler dados de entrada.
n = int(input())
v = list(map(int, input().split()))

# Percorrer valores...
t = 0
c = 1
for i in range(1, n):
    if v[i] == v[i - 1]:
        c += 1  # ... calculando o tamanho de sequências de valores iguais...
    else:
        t = max(t, c)  # ... e mantendo o tamanho da maior sequência encontrada.
        c = 1

print(max(t, c))  # Lembrar de considerar a última sequência, também.

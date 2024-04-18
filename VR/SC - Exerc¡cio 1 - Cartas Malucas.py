# Ler dados de entrada.
n = int(input())
v = list(map(int, input().split()))

# Percorrer a sequência de cartas contando a quantidade de vezes que a progressão muda.
j = 0
i = 1
resp = 1
while i < n:
    if v[i] - v[i - 1] != v[j + 1] - v[j]:  # Houve mudança na progressão!
        j = i
        i += 1
        resp += 1
    i += 1

# Exibir contagem.
print(resp)

# Ler dados de entrada.
n = int(input())
postes = []
for i in range(n):
    postes.append(int(input()))

# Forma simples de lidar com circularidade. Outras opções são:
# - Usar indexação negativa; e
# - Utilizar resto da divisão para corrigir o índice.
for i in range(n):
    postes.append(postes[i])

# Dar a volta do prédio contando o tamanho das sequências de lapadas fracas.
maior = 0
atual = 0
for i in range(2*n-1):
    if postes[i] + postes[i+1] < 1000:
        atual += 1
        if atual > maior:
            maior = atual
    else:
        atual = 0

if maior > n:
    maior = n

# Reportar a maior sequência.
print(maior)

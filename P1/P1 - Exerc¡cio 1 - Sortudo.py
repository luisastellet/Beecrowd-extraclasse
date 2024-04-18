# Ler a quantidade N de jogadores, a quantidade T de turnos e os N*T números da sorte
n, t = map(int, input().split())
numeros_da_sorte = list(map(int, input().split()))

# Distribuir os números da sorte organizando a pontuação em uma lista circular de jogadores
pontuacao = [0] * n
for i in range(n * t):
    pontuacao[i % n] += numeros_da_sorte[i]

# Buscar pelo jogador com maior pontuação
maior = pontuacao[0]
jogador = 0
for i in range(1, n):
    if pontuacao[i] >= maior:  # O uso de maior ou igual garante que em caso
        maior = pontuacao[i]   # de empate o último a jogar será o vencedor
        jogador = i

# Exibir o jogador vencedor
print(jogador + 1)

# Guardar a pontuação das cartas como o íncide de uma lista para simplificar a implementação.
ORDEM_DAS_CARTAS = [4, 5, 6, 7, 12, 11, 13, 1, 2, 3]

# Inicializar contadores de partidas vencidas.
vitorias_tim = 0
vitorias_mais = 0

# Para cada partida...
n = int(input())
for _ in range(n):
    # Ler as cartas jogadas.
    cartas = list(map(int, input().split()))
    # Obter a pontuação associada às cartas jogadas
    pontos = [None] * 6
    for i in range(6):
        pontos[i] = ORDEM_DAS_CARTAS.index(cartas[i])
    
    # Verificar quem venceu cada jogada.
    tim = 0
    maia = 0
    for i in range(3):
        if pontos[i] >= pontos[i+3]:
            tim += 1
        else:
            maia += 1

    # Atualizar contadores de partidas vencidas.
    if tim > maia:
        vitorias_tim += 1
    else:
        vitorias_mais += 1

# Mostrar contagem final.
print(vitorias_tim, vitorias_mais)

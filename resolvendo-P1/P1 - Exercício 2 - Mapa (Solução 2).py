# Para cada conjunto de teste faça
t = 1
n = int(input())
while n != -1:
    # Avaliar a expressão final que conta quantos pedaços de mapa foram obtidos
    print('Teste', t)
    print((2**n + 1)**2)
    print()

    t += 1
    n = int(input())

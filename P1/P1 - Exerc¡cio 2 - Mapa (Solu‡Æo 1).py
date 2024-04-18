# Para cada conjunto de teste faça
t = 1
n = int(input())
while n != -1:
    # Inicializar as variáveis auxiliares de contagem de linhas
    anterior, atual = 2, 2

    # Para cada par de dobras executadas, atualize a contagem de linhas
    for _ in range(n):
        atual = 2 * anterior - 1
        anterior = atual  # O valor atual será o anterior caso existe outra iteração

    # A contagem de linhas e de colunas é simétrica, logo o resultado é o quadrado da contagem atual
    print('Teste', t)
    print(atual**2)
    print()

    t += 1
    n = int(input())

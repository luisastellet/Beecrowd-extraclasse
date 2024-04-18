# Ler tamanho da pirâmide
n = int(input())

# Inicializar matriz com uns.
piramide = [[1] * n for _ in range(n)]  # Existem outras formas de inicializar... só quiz ser econômico nas linhas

# Da camada 2 em diante...
for k in range(2, 2+n//2):
    # Montar linha superior
    for i in range(k-1, n-k+1):
        piramide[k-1][i] = k
    # Montar linha inferior
    for i in range(k-1, n-k+1):
        piramide[n-k][i] = k        
    # Montar coluna esquerda
    for j in range(k-1, n-k+1):
        piramide[j][k-1] = k        
    # Montar coluna direita
    for j in range(k-1, n-k+1):
        piramide[j][n-k] = k        

    
# Mostrar resultado
for i in range(n):
    for j in range(n-1):
        print(piramide[i][j], end=' ')  # Utilizar end para impedir quebra de linha
    print(piramide[i][n-1])

n = int(input())
teste = 4
for i in range(n):
    linhas_colunas = int(input())
    matriz = []

    for i in range(linhas_colunas):
        matriz.append(list(map(int,input().split())))

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = matriz[i][j] ** 2

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = str(matriz[i][j]) 

    print(f'Quadrado da matriz #{teste}:')

    for i in range(linhas_colunas):
        tamanhos = []
        for j in range(linhas_colunas):
            tamanhos.append(len(matriz[j][i]))
            tamanhos.sort(reverse=True)
        lenmaior = tamanhos[0]
  
        for x in range(linhas_colunas):
            matriz[x][i] = (' ' * (lenmaior - len(matriz[x][i]))) + matriz[x][i]
        
    for z in range(linhas_colunas):
        resp = ''
        for y in range(linhas_colunas):
            resp += matriz[z][y]
            if y != linhas_colunas -1:
                resp += ' '
        print(resp)
    if i != n-1:
        print()
    teste +=1
    

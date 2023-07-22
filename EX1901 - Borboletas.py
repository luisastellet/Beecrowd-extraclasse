n = int(input()) #tamanho da floresta
matriz = []
visitados = []
unicas = 0

for i in range(n):
    matriz.append(list(map(int,input().split())))

for i in range(n*2):
    linha,coluna = map(int,input().split())
    linha -= 1 #indices reais
    coluna-= 1 #indeices reais
    if matriz[linha][coluna] not in visitados:
        visitados.append(matriz[linha][coluna])

print(len(visitados))
def funcaoaux(matriz,l1,c1):
    if l1 < 0 or c1 < 0 or l1 > len(matriz)-1 or c1 > len(matriz[0])-1:
        return 0
    return matriz[l1][c1]

def funcao(matriz,l1,c1,l2,c2):
    x1 = funcaoaux(matriz,l2,c2)
    x2 = funcaoaux(matriz,l1-1,c2)
    x3 = funcaoaux(matriz,l2,c1-1)
    x4 = funcaoaux(matriz,l1-1,c1-1)
    return x1-x2-x3+x4


#recebendo dados de linhas e colunas
linhas_plantacao, colunas_plantacao, linhas_lote, colunas_lote = map(int,input().split())

#recebendo a matriz da plantacao
plantacao = []
for i in range(linhas_plantacao):
    plantacao.append(list(map(int,input().split())))

#parede de cima
for i in range(1,colunas_plantacao):
    plantacao[0][i] = plantacao[0][i-1] + plantacao[0][i]
#parede da esquerda
for j in range(1,linhas_plantacao):
    plantacao[j][0] = plantacao[j-1][0] + plantacao[j][0]

for i in range(1,linhas_plantacao):
    for j in range(1,colunas_plantacao):
        plantacao[i][j] = plantacao[i][j-1] + plantacao[i-1][j] - plantacao[i-1][j-1] + plantacao[i][j]

# for i in range(linhas_plantacao):
#     for j in range(colunas_plantacao):
#         print(plantacao[i][j],end=' ')
#     print()

maior = -1000000

for i in range(linhas_plantacao):
    for j in range(colunas_plantacao):
        maior = max(maior,funcao(plantacao,i,j,i+linhas_lote-1,j+colunas_lote-1))
print(maior)
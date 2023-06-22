linhas, colunas = map(int,input().split())
#n linhas seguintes contêm m inteiros
linha = []

maior = 0
for i in range(linhas):
    linha.append(list(map(int,input().split())))
for i in range(linhas):
    resultado = 0
    for j in range(colunas):
        resultado += linha[i][j]
    if resultado > maior:
        maior = resultado

for i in range(colunas):
    resultado = 0
    for j in range(linhas):
        resultado += linha[j][i]
    if resultado > maior:
        maior = resultado

print(maior)
numero_paises = int(input())
matriz = []
for i in range(numero_paises):
    dados = list(input().split())
    dados[1] = int(dados[1]) #ouro
    dados[2] = int(dados[2]) #prata
    dados[3] = int(dados[3]) #bronze
    matriz.append(dados)

for j in range(len(matriz)-1):
    for i in range(len(matriz)-1):
        teste = []
        if matriz[i+1][1] > matriz[i][1]:
            aux = matriz[i]
            matriz[i] = matriz[i+1]
            matriz[i+1] = aux
        elif matriz[i+1][1] == matriz[i][1]:
            if matriz[i+1][2] > matriz[i][2]:
                aux = matriz[i]
                matriz[i] = matriz[i+1]
                matriz[i+1] = aux
            elif matriz[i][2] == matriz[i+1][2]:
                if matriz[i+1][3] > matriz[i][3]:
                    aux = matriz[i]
                    matriz[i] = matriz[i+1]
                    matriz[i+1] = aux
                elif matriz[i][3] == matriz[i+1][3]:
                    if matriz[i][0] > matriz[i+1][0]:
                        aux = matriz[i]
                        matriz[i] = matriz[i+1]
                        matriz[i+1] = aux
for i in range(len(matriz)):
    resp = ''
    for j in range(len(matriz[i])):
        resp += str(matriz[i][j]) + ' '
    print(resp.strip())
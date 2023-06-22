N = int(input())
M = []
ganhou = []
trilha = 1
for i in range(N):
    dados = list(map(int,input().split()))
    M.append(dados[0])
    dados.pop(0)
    tamanho = len(dados) #diz quantos H teve
    #frente pra trás
    esf_frente = 0
    for c in range(tamanho - 1):
        if dados[c+1] - dados[c] > 0:
            esf_frente += (dados[c+1] - dados[c])

    #trás pra frente
    esf_tras = 0
    dados_inv = []
    for s in range(tamanho-1, -1, -1):
        dados_inv.append(dados[s])

    for j in range(tamanho - 1):
        if dados_inv[j+1] - dados_inv[j] > 0:
            esf_tras += (dados_inv[j+1] - dados_inv[j])

    if esf_frente < esf_tras:
        ganhou.append(esf_frente)
    elif esf_tras < esf_frente:
        ganhou.append(esf_tras)
    else: 
        ganhou.append(esf_frente)

ganhador = ganhou[0] #sentinela
for k in range(1, len(ganhou)):
    if ganhou[k] < ganhador:
        ganhador = ganhou[k]
        trilha = k+1
print(trilha)

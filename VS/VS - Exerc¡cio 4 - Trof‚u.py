# Ler pontuação
pontos = [int(input()) for _ in range(5)]

# Ordenar de forma decrescente
pontos.sort(reverse=True)

# Identificar primeira ocorrência de cada pontuação
ind_primeiro = 0
ind_segundo = 1
ind_terceiro = 2
for ind in range(1, 5):
    if pontos[ind_primeiro] == pontos[ind]:
        ind_segundo = ind + 1
        ind_terceiro = ind + 2
    elif pontos[ind_segundo] == pontos[ind]:
        ind_terceiro = ind + 1

# Calcular número de troféus e placas
trofeus = ind_segundo - ind_primeiro
placas = ind_terceiro - ind_segundo

# Mostrar resultado
print(trofeus, placas)

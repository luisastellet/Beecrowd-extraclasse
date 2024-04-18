# Inicializar listas constantes auxiliares
FIGURA               = ['A', 'J', 'Q', 'K']
PONTOS_DOMINANTE     = [ 14,  15,  16,  17]
PONTOS_NAO_DOMINANTE = [ 10,  11,  12,  13]

# Identificar o naipe dominante
_, naipe_dominante = list(input())

# Calcular pontuação de Luana
pontos_luana = 0
for _ in range(3):
    figura, naipe = list(input())
    ind_figura = FIGURA.index(figura)
    if naipe == naipe_dominante:
        pontos_luana += PONTOS_DOMINANTE[ind_figura]
    else:
        pontos_luana +=  PONTOS_NAO_DOMINANTE[ind_figura]

# Calcular pontuação de Edu
pontos_edu = 0
for _ in range(3):
    figura, naipe = list(input())
    ind_figura = FIGURA.index(figura)
    if naipe == naipe_dominante:
        pontos_edu += PONTOS_DOMINANTE[ind_figura]
    else:
        pontos_edu +=  PONTOS_NAO_DOMINANTE[ind_figura]

# Mostrar resultado
if pontos_edu > pontos_luana:
    print('Edu')
elif pontos_luana > pontos_edu:
    print('Luana')
else:
    print('empate')

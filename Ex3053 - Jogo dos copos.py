n = int(input())
posição_inicial = input()
for i in range(n):
    movimento = int(input())
    if movimento == 1:
        if posição_inicial == 'A':
            posição_inicial = 'B'
        elif posição_inicial == 'B':
            posição_inicial = 'A'
    elif movimento == 2:
        if posição_inicial == 'B':
            posição_inicial = 'C'
        elif posição_inicial == 'C':
            posição_inicial = 'B'
    else:
        if posição_inicial == 'A':
            posição_inicial = 'C'
        elif posição_inicial == 'C':
            posição_inicial = 'A'
print(posição_inicial)

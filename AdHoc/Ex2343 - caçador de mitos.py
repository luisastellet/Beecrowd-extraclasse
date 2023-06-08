N = int(input()) #número de raios registrados
coordenadas = []
raios = 0
for i in range(N):
    coordenadas.append(input()) #coordenadas no quadrante
for j in range(N):
    if coordenadas.count(coordenadas[j]) > 1:
        raios = 2
        break

if raios == 2:
    print('1')
else:
    print('0')




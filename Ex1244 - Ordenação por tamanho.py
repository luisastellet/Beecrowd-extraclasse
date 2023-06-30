casos = int(input())
for i in range(casos):
    strings = input().split()
    matriz = []
    for j in range(len(strings)):
        matriz.append(strings[j])
    ordenado = sorted(matriz, reverse=True, key=len)
    resp = ''
    for x in range(len(ordenado)):
        resp += ordenado[x] + ' '
    print(resp.strip())

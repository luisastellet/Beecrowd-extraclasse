l, c, m, n = map(int,input().split())
plantacao = []
for i in range(l):
    plantacao.append(list(map(int,input().split())))
maior = 0
for i in range(0,l,m):
    for j in range(0,c,n):
        margaridas = 0
        for k in range(i,m+i):
            for p in range(j,n+j):
                margaridas += plantacao[k][p]
        if margaridas > maior:
            maior = margaridas
print(maior)


l, c, m, n = map(int, input().split())
plantacao = []
for i in range(l):
    plantacao.append(list(map(int,input().split())))
maior = 0
for i in range(0,l,m):
    for j in range(0,c,n):
        margaridas = 0
        for k in range(i, i+m):
            for p in range(j, j+n):
                margaridas += plantacao[k][p]
        if margaridas > maior:
            maior = margaridas
print(maior)

l,c,m,n = map(int,input().split())
plantacao = []
for i in range(l):
    plantacao.append(list(map(int,input().split())))
maior = 0
for i in range(0,l,m):
    for j in range(0,c,n):
        margaridas = 0
        for k in range(i,m+i):
            for p in range(j,n+j):
                margaridas += plantacao[k][p]
        if margaridas > maior:
            maior = margaridas
print(maior)
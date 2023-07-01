p = list(map(int,input().split()[1:]))
m = list(map(int,input().split()[1:]))
f = list(map(int,input().split()[1:]))
q = list(map(int,input().split()[1:]))
b = list(map(int,input().split()[1:]))
k = int(input())
lista = []
for P in p:
    for M in m:
        for F in f:
            for Q in q:
                for B in b:
                    lista.append(P+M+F+Q+B)
lista.sort(reverse=True)
soma = 0
for i in range(k):
    soma += lista[i]
print(soma)
n, t = map(int,input().split())
lista = list(map(int,input().split()))
jogadores = [0] * n

for i in range(n):
    soma = 0
    for j in range(i, len(lista),n):
        soma += lista[j]
    jogadores[i] = soma

maior = jogadores[0]
resposta = 1 #indice + 1 
for x in range(len(jogadores)):
    if jogadores[x] >= maior:
        maior = jogadores[x]
        resposta = x+1
print(resposta)

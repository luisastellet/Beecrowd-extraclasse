N = int(input())
pilha_inicial = [int(_) for _ in input().split()]
soma1 = sum(pilha_inicial)
pilha_final = [int(_) for _ in range(1, N + 1)]
soma2 = sum(pilha_final)
for _ in range(1):
    if soma2 != soma1:
        soma2 = soma1 - soma2
        if soma2 % N != 0:
            print(-1)
            break
        for add in range(N):
            pilha_final[add] += soma2 / N
    movidos = 0
    while len(pilha_inicial) > 0:
        coluna1 = pilha_inicial[0]
        coluna2 = pilha_final[0]
        if coluna1 > coluna2:
            movidos += (coluna1 - coluna2)
        pilha_inicial.remove(coluna1)
        pilha_final.remove(coluna2)
    print(int(movidos))

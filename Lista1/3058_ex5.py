# #EXERCÍCIO 5:
N = int(input())
menor = float('inf')
for i in range(N):
    P, G = input().split()
    P = float(P)
    G = int(G)
    valorgrama = P / G
    if valorgrama < menor:
        menor = valorgrama
print(menor * 1000)
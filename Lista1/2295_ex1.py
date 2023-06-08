#EXERCÍCIO 1
A, G, Ra, Rg = map(float, input().split())
distA = Ra / A
distG = Rg / G
if distA > distG:
    print('A')
else:
    print('G')
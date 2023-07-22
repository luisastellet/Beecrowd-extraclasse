carros, voltas = map(int,input().split())
tempos = []
for i in range(carros):
    dados = list(map(int,input().split()))
    tempos.append(sum(dados))
tempos_ord = sorted(tempos)

primeiro = tempos.index(tempos_ord[0])
segundo = tempos.index(tempos_ord[1])
terceiro = tempos.index(tempos_ord[2]) 
print(primeiro + 1)
print(segundo + 1)
print(terceiro + 1)
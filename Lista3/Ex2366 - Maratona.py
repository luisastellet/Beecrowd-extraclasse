#um copo -> +2000 metros = DIM
#if distancia entre dois postos de agua <= DIM(2000):
    #consegue terminar a corrida
#else:
    #nao consegue terminar a prova

N, M = map(int,input().split())
#N é o numero de postos de agua
#M é a distancia maxima de cada atleta apos beber agua
postos = list(map(int,input().split()))
postos.append(42195)
verificador = True
for i in range(1,N+1):
    if postos[i] - postos[i-1] > M:
        verificador = False
        break
if verificador == False:
    print('N')
else:
    print('S')

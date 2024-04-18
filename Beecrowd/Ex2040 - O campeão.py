#vencedr = 5 pontos
#empate = 1 ponto para cada
#gol = 3 pontos
import math
times = int(input())
while times != 0:
    infos = []
    for i in range(times):
        infos.append(input().split())
        infos[i][1] = int(infos[i][1]) #linha indica os dados, ai a posição 0 indica o nome e a posicao 1 indica os pontos
    x = math.trunc(times/2)
    pontos = []
    for i in range(x):
        placar = input().split()
        placar[1] = placar[1].split('-')
        placar[1][0] = int(placar[1][0])
        placar[1][1] = int(placar[1][1])
        pontos.append(placar)

    for y in range(len(pontos)): #primeiro placar
        for j in range(times):
            if pontos[y][0] == infos[j][0]:
                pos1 = j #primeiro time o nome dele
            if pontos[y][2] == infos[j][0]:
                pos2 = j #segundo time o nome dele

        #analisando os pontos e corrigindo
        if pontos[y][1][0] > pontos[y][1][1]:
            infos[pos1][1] += 5 + pontos[y][1][0]*3
            infos[pos2][1] += pontos[y][1][1]*3
        elif pontos[y][1][0] < pontos[y][1][1]:
            infos[pos1][1] += pontos[y][1][0]*3
            infos[pos2][1] += 5 + pontos[y][1][1]*3
        else:
            infos[pos1][1] += 1 + pontos[y][1][0]*3 
            infos[pos2][1] += 1 + pontos[y][1][1]*3

    infos.sort(key=lambda x:x[1], reverse=True)
    if infos[0][0] == 'Sport':
        print(f"O Sport foi o campeao com {infos[0][1]} pontos :D")
    else:
        print(f"O Sport nao foi o campeao. O time campeao foi o {infos[0][0]} com {infos[0][1]} pontos :(")
    print()
    times = int(input())
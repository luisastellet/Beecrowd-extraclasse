P = 1
R = 1
teste = 1
while P != 0 and R != 0:
    P, R = map(int, input().split())
    if P != 0 and R != 0:
        ordem_inicio = list(map(int,input().split())) #uma lista com P elementos
        for i in range(R):
            #rodadas
            dados = list(map(int,input().split()))
            N = dados[0]
            J = dados[1]
            dados.remove(N)
            dados.remove(J)
            pos = 0
            for c in range(N):
                if dados[c] != J:
                    ordem_inicio.remove(ordem_inicio[pos])
                else:
                    pos += 1
        print('Teste', teste)
        print(ordem_inicio[0])
        print()
        teste += 1


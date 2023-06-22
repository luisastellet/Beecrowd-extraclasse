N=1
testes = 1 
while N != 0:
    N = int(input(''))
    if N != 0:
        jogador1 = input('')
        jogador2 = input('')
        ganhador = []
        for i in range(N):
            valores = input('').split()
            j1 = int(valores[0])
            j2 = int(valores[1])
            if (j1 + j2) % 2 == 0:
                ganhador.append(jogador1)
            else:
                ganhador.append(jogador2)
        print('Teste', testes)
        testes += 1
        for c in range(len(ganhador)):
            print(ganhador[c])
        print()

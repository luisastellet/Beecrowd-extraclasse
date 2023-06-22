import math
N = 1
M = 1
#N = número de medições
#M = intervalo de tempo
teste = 1
while N != 0 and M != 0:
    N, M = map(int, input().split())
    if N != 0 and M != 0:
        temperatura = []
        lista_soma = []
        aux = 0
        for i in range(N):
            temperatura.append(int(input()))

        for j in range(N):
            soma = temperatura[j] + aux
            aux = soma
            lista_soma.append(soma)

        menor = lista_soma[M-1]/M
        maior = lista_soma[M-1]/M
        for i in range(M, len(lista_soma)-M):
            if (lista_soma[i] - lista_soma[i-M])/M < menor:
                menor = (lista_soma[i] - lista_soma[i-M])/M
            if (lista_soma[i] - lista_soma[i-M])/M > maior:
                maior = (lista_soma[i] - lista_soma[i-M])/M
        #NÃO ENTENDEI AS RESTRIÇÕES DESSE FOR
        #for c in range(M-1, len(lista_soma), 1):
            #NÃO ENTENDI A CONTA DESSE IF E DO ELSE
            #if c == M-1:
                #menor = (lista_soma[c])/M
                #maior = (lista_soma[c])/M
            #else:
                #if (lista_soma[c] - lista_soma[c-M])/M > maior:
                    #maior = (lista_soma[c] - lista_soma[c-M])/M
                #if (lista_soma[c] - lista_soma[c-M])/M < menor:
                    #menor = (lista_soma[c] - lista_soma[c-M])/M
        menor = math.trunc(menor)
        maior = math.trunc(maior)
        print("Teste", teste)
        print(menor, maior)
        print()
        teste += 1

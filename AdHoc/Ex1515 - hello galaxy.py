N = int(input())
while N != 0:
    nomes = []
    ano = []
    duracao = []
    for i in range(N):
        dados = input().split()
        nomes.append(dados[0])
        ano.append(int(dados[1]))
        duracao.append(int(dados[2]))
    lista = []
    for i in range(N):
        lista.append(ano[i] - duracao[i])
    menor = lista[0]
    nome = nomes[0]
    for i in range(1,N):
        if lista[i] < menor:
            menor = lista[i]
            nome = nomes[i]
    print(nome)
    N = int(input())
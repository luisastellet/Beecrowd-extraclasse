N = int(input())
for i in range(N):
    palavras = input().strip().split()
    resposta = ''
    for j in range(len(palavras)):
        resposta += palavras[j][0]
    print(resposta)

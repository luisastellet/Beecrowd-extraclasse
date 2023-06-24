linhas = int(input())
colunas = int(input())
if linhas % 2 == 0:
    if colunas % 2 == 0:
        resposta = 1
    else:
        resposta = 0
else:
    if colunas % 2 == 0:
        resposta = 0
    else:
        resposta = 1
print(resposta)
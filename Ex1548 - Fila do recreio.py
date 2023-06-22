testes = int(input())
for i in range(testes):
    cont = 0
    alunos = int(input())
    notas = list(map(int, input().split()))
    notas_certa = sorted(notas, reverse=True)
    for j in range(alunos):
        if notas[j] == notas_certa[j]:
            cont += 1
    print(cont)
#EXERCÍCIO 2
I, N = input().split()
Iint = int(I)
Nint = int(N) #número que aparecerá no for (númeor de vezes da análise)
D = Iint
E = Iint
F = Iint
for i in range(Nint):
    operacao = input().split()
    valor = int(operacao[len(operacao)-1])
    if operacao[0] == 'C':
        if operacao[1] == 'D':
            D -= valor
        elif operacao[1] == 'E':
            E -= valor
        else:
            F -= valor
    if operacao[0] == 'V':
        if operacao[1] == 'D':
            D += valor
        elif operacao[1] == 'E':
            E += valor
        else:
            F += valor
    if operacao[0] == 'A':
        if operacao[1] == 'D':
            if operacao[2] == 'E':
                D += valor
                E -= valor
            if operacao[2] == 'F':
                D += valor
                F -= valor
        elif operacao[1] == 'E':
            if operacao[2] == 'D':
                E += valor
                D -= valor
            if operacao[2] == 'F':
                E += valor
                F -= valor
        else:
            if operacao[2] == 'E':
                F += valor
                E -= valor
            if operacao[2] == 'D':
                F += valor
                D -= valor
print(D, E, F)
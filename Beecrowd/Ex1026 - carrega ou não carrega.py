def binario(num):
    lista = []
    while num // 2 != 0:
        lista.append(num % 2)
        num = num // 2
    lista.append(num % 2)
    lista.sort(reverse=True)
    if len(lista) < 8:
        for i in range(8-len(lista)):
            lista.insert(0,0)
    return lista

def decimal(lista):
    total = 0
    for i in range():
        if lista[i] != ' ':
            total += lista[i]**(len(resp)-i-1)
    return total

while True:
    try:
        a, b = map(int, input().split())
        listaA = binario(a)
        listaB = binario(b)
        compA = [0] * (32-len(str(listaA)))
        listaA = compA + listaA
        compB = [0] * (32-len(str(listaB)))
        listaB = compB + listaB
        for i in range(8, len(listaA), 8):
            listaA.insert(i,' ')
        for i in range(8, len(listaB), 8):
            listaB.insert(i,' ')

        resp = [0] * 35
        print(len(listaA))
        print(len(listaB))
        for i in range(35):
            if listaA[i] == ' ':
                resp[i] = ' '
            if listaA[i] + listaB[i] == 0:
                resp[i] = 0
            elif listaA[i] + listaB[i] == 1:
                resp[i] = 1
            elif listaA[i] + listaB[i] == 2:
                resp[i] = 0

        print(decimal(resp))

    except EOFError:
        break
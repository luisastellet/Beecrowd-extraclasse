while True:
    try:
        n = int(input())
        lista = list(map(int,input().split()))
        chegar = sum(lista) / n
        passos = 1
        if sum(lista) % n == 0:
            passos += (lista[-1] - chegar)
            print(f"{passos:.0f}")
        else:
            print('-1')
    except EOFError:
        break
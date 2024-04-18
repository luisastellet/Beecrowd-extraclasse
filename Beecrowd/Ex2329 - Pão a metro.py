N = int(input())
K = int(input())
v = [int(i) for i in input().split()]
def fatia(x):
    total = 0
    for i in v:
        total += i // x
    if total >= N: return True
    else: return False

inicio = 0
fim = (sum(v) // N) + 1
meio = (inicio + fim) // 2

while True:
    if fatia(meio):
        if not fatia(meio+1):
            print(meio)
            break
        else:
            inicio = meio
            meio = (inicio + fim) // 2
    else:
        fim = meio
        meio = (inicio + fim) // 2
inicio = list(map(int,input().split()))
ordem = []
if inicio[0] < inicio[1] and inicio[0] < inicio[2]:
    menor = inicio[0]
    if inicio[1] < inicio[2]:
        meio = inicio[1]
        maior = inicio[2]
    else:
        meio = inicio[2]
        maior = inicio[1]

elif inicio[1] < inicio[2] and inicio[1] < inicio[0]:
    menor = inicio[1]
    if inicio[0] < inicio[2]:
        meio = inicio[0]
        maior = inicio[2]
    else:
        meio = inicio[2]
        maior = inicio[0]
else:
    menor = inicio[2]
    if inicio[0] < inicio[1]:
        meio = inicio[0]
        maior = inicio[1]
    else:
        meio = inicio[1]
        maior = inicio[0]


print(menor)
print(meio)
print(maior)
print()
for c in range(3):
    print(inicio[c])

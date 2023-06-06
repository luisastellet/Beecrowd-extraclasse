cont = 0
positivos = []
for i in range(6):
    n = float(input())
    if n > 0:
        cont += 1
        positivos.append(n)
soma = 0
for c in range(len(positivos)):
    soma += positivos[c]

media = soma / cont
print(f"{cont} valores positivos")
print(f"{media:.1f}")

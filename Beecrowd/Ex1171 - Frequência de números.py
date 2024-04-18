vezes = int(input())
lista = []
for i in range(vezes):
    lista.append(int(input()))
lista.sort()
for i in range(vezes):
    if lista.index(lista[i]) == i:
        cont = lista.count(lista[i])
        print(f"{lista[i]} aparece {cont} vez(es)")
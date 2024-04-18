# Ler dados de entrada.
n = int(input())
preco = []
for i in range(n):
    preco.append(int(input()))

# Ordenar do maior para o menor preço.
preco.sort(reverse=True)

# Soma preços, sem usar os gratuitos.
soma = 0
for i in range(n):
    if i % 3 != 2:
        soma += preco[i]

# Mostrar total a pagar.
print(soma)

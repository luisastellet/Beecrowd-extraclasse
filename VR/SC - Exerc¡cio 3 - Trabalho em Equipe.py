# Ler peso carregado e aproveitar para obter o somatório.
soma = 0
pesos = []
n = int(input())
for i in range(n):
    p = int(input())
    soma += p
    pesos.append(p)

# Calcular a distribuição justa de peso.
ideal = soma // n

# Reportar o alívio ou a carga extra de cada estudante.
for p in pesos:
    print(ideal - p)

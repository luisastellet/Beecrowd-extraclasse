# Ler dados de entrada.
n = int(input())
a = list(map(int, input().split()))

# Somar as alturas das extremidades para o centro, verificando se as somas são todas iguais.
h = a[0] + a[n - 1]
i = 1
j = n - 2
while i <= j and a[i] + a[j] == h:
    i += 1
    j -= 1

# Caso sejam todas iguais, sinalizar que o perfil é ortogonal.
if i > j:
    print("S")
else:
    print("N")

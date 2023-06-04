cod, quant = list(map(int,input().split()))
if cod == 1:
    preco = 4.0
elif cod == 2:
    preco = 4.5
elif cod == 3:
    preco = 5.0
elif cod == 4:
    preco = 2.0
elif cod == 5:
    preco = 1.5

valor = preco * quant
print(f"Total: R$ {valor:.2f}")
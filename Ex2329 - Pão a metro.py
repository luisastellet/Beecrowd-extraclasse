# (paes * tamanho) / pessoas = tamanho_fatia
pessoas = int(input())
sanduiches = int(input())
tamanhos = list(map(int,input().split())) #tamanho da lista = sanduiches (de 0 até sanduiches-1)
tamanhos.sort() # 98 99 100
tamanhos_inv = list(reversed(tamanhos)) # 100 99 98
medida = tamanhos_inv[1]
pedacos = 0
while pedacos < pessoas:
    pedacos = 0
    for i in range(sanduiches):
        pedacos += tamanhos_inv[i] // medida
        if tamanhos_inv[i] == medida and pedacos == pessoas:
            break
    if pedacos < pessoas:
        medida -= 1
print(medida)

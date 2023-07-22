postos, qntdcarros, qntdchecagem = map(int, input().split())
corrida = []
checagem = {}
for i in range(qntdchecagem):
    x, y = map(int,input().split())
    checagem['carro'] = x
    checagem['posto'] = y
    corrida.append(checagem.copy())
    
cont = [0]*qntdcarros

for i in range(qntdcarros):
    ver = 1
    for j in range(qntdchecagem):
        if corrida[j]['carro'] == i+1 and corrida[j]['posto'] == ver:
            ver += 1
            cont[i] += 1
            if ver == postos:
                ver = 1
ordenado = sorted(cont, reverse=True)
max = ordenado[0]

res = ''
for i in range(qntdcarros):
    res += str(cont.index(ordenado[i])+1) + ' '
print(res.strip())
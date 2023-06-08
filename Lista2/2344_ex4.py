#EXERCÍCIO 4
bandejas = int(input())
quebrados = 0
for i in range(bandejas):
    infos = input().split()
    L = int(infos[0])
    C = int(infos[1])
    if L > C:
        quebrados += C
    L = 0
    C = 0
print(quebrados)
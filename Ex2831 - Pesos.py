#P - Q <= 8
#P = pewso da cabine mais pedasa
#Q = peso da cabine mais leve
n = int(input())
peso = list(map(int,input().split()))
#indice do último: n-1
if peso[0] > 8: #se o primeiro peso já é maior, não vai dar, já que estão na ordem de peso
    print('N')
else:
    verificador = True
    for i in range(1,len(peso)):
        if peso[i] - peso[i-1] > 8:
            verificador = False
            break
    if verificador:
        print('S')
    else:
        print('N')
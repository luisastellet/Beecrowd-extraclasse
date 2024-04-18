hora1, minuto1, hora2, minuto2 = map(int,input().split())
tempos = []
while hora1 !=0 or minuto1 != 0 or hora2 != 0 or minuto2 != 0:
    if hora1 == 0:
        hora1 = 24 * 60
    else:
        hora1 *= 60
        
    if hora2 == 0:
        hora2 = 24 * 60
    else:
        hora2 *= 60

    tempo1 = hora1 + minuto1
    tempo2 = hora2 + minuto2
    if tempo2 < tempo1:
        tempo2 = hora2 + minuto2 + 1440

    tempos.append(abs(tempo2 - tempo1))

    hora1, minuto1, hora2, minuto2 = map(int,input().split())
    
for resp in tempos:
    print(resp)

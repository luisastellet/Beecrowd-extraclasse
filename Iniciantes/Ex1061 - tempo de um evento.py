# diaf = input().split()
# diaf = int(diaf[1])
# fim = input().split()
# fim.pop(1)
# fim.pop(2)
# fim = list(map(int, fim))

# if fim[0] < inicio[0]: # hora final < hora inicial
#     dia = diaf - diai - 1
#     horas = 24 - (inicio[0] - fim[0])
#     if #minuto final < minuto inicial
#         minutos = fim[1] - inicio[1] - 1

#         if #segundo final < segundo inicial
#             segundos = fim[2]
#         else: #segundo final > segundo inicial

#     else: # minuto final > minuto inicial
#         minutos = fim[1] - inicio[1]

# else: #hora final > hora inicial

#     print(f"{dia} dia(s)")
#     print(f"{horas} hora(s)")

    dia_i = input().split()
    hora_i = input().split()
    dia_f = input().split()
    hora_f = input().split()
    di, df = int(dia_i[1]), int(dia_f[1])
    hi, mi, si = int(hora_i[0]), int(hora_i[2]), int(hora_i[4])
    hf, mf, sf = int(hora_f[0]), int(hora_f[2]), int(hora_f[4])

    minuto_seg = 60
    hora_seg = minuto_seg * 60
    dia_seg = hora_seg * 24
    i = si + mi * minuto_seg + hi * hora_seg + di * dia_seg
    f = sf + mf * minuto_seg + hf * hora_seg + df * dia_seg
    if i < f:
        tempo = f - i
        dias = int(tempo / dia_seg)
        tempo = tempo % dia_seg
        horas = int(tempo / hora_seg)
        tempo = tempo % hora_seg
        minutos = int(tempo / minuto_seg)
        tempo = tempo % minuto_seg
        segundos = tempo
        print('{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)'.format(dias, horas, minutos, segundos))
jogadores = 128
contador_de_partidas = 0
numero_de_partidas_por_fase = 128
while numero_de_partidas_por_fase > 1:
    
    if numero_de_partidas_por_fase > 1:
        numero_de_partidas_por_fase = numero_de_partidas_por_fase / 2
        jogadores = 128 - contador_de_partidas
        contador_de_partidas += numero_de_partidas_por_fase

    print(numero_de_partidas_por_fase, contador_de_partidas, jogadores)
print('O campeonato teve um total de {:.0f} partidas' .format(contador_de_partidas))
while True:
    try:
        hora, minuto = map(int,input().split(':'))
        tempo = hora*60 + minuto + 60
        atraso = tempo - 8*60
        if atraso < 0:
            print(f'Atraso maximo: 0')
        else:
            print(f'Atraso maximo: {atraso}')

    except EOFError:
        break
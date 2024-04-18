while True:
    try:
        atributos = int(input())
        marcos, leonardo = map(int,input().split())
        cartasM = []
        cartasL = []
        for i in range(marcos):
            cartasM.append(list(map(int,input().split())))
        for i in range(leonardo):
            cartasL.append(list(map(int,input().split())))
        cartaM, cartaL = map(int, input().split())
        
        atributo = int(input())
        
        if cartasM[cartaM-1][atributo-1] > cartasL[cartaL-1][atributo-1]:
            print('Marcos')
        elif cartasM[cartaM-1][atributo-1] < cartasL[cartaL-1][atributo-1]:
            print('Leonardo')
        else:
            print('Empate')

    except EOFError:
        break
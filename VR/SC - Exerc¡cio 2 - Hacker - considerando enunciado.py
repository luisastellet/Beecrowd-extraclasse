import math

# Definir uma função que verifica se o número é Super Fantástico.
def super_fantastico(n):
    # Para os dígitos é fácil, pois são apenas 10. Nem precisa calcular.
    for i in range(len(n)):
        if n[i] == '0' or n[i] == '4' or n[i] == '6' or n[i] == '8' or n[i] == '9':
            return False
    # Para o número principal o processo é semelhante à verificação de número primo.
    n = int(n)
    if n < 1:
        return False
    elif n != 2:
        for x in range(2, int(math.sqrt(n)) + 1):
            if(n % x==0):
                return False
    return True


# Para cada número, reportar se ele é Super Fantástico ou Normal.
num = input()
while num != '0':
    if super_fantastico(num):
        print('Super')
    else:
        print('Normal')
    num = input()

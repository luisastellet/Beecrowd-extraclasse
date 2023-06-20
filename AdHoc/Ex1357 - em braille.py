D = int(input())
while D != 0:
    tipo = input()
    if tipo == "S":
        digitos = input()
        linha1 = ''
        linha2 = ''
        linha3 = ''
        for numero in digitos:
            if numero == '1':
                linha1 += '*.' + ' '
                linha2 += '..' + ' '
                linha3 += '..' + ' '
            elif numero == '2':
                linha1 += '*.' + ' '
                linha2 += '*.' + ' '
                linha3 += '..' + ' '
            elif numero == '3':
                linha1 += '**' + ' '
                linha2 += '..' + ' '
                linha3 += '..' + ' '
            elif numero == '4':
                linha1 += '**' + ' '
                linha2 += '.*' + ' '
                linha3 += '..' + ' '
            elif numero == '5':
                linha1 += '*.' + ' '
                linha2 += '.*' + ' '
                linha3 += '..' + ' '
            elif numero == '6':
                linha1 += '**' + ' '
                linha2 += '*.' + ' '
                linha3 += '..' + ' '
            elif numero == '7':
                linha1 += '**' + ' '
                linha2 += '**' + ' '
                linha3 += '..' + ' '
            elif numero == '8':
                linha1 += '*.' + ' '
                linha2 += '**' + ' '
                linha3 += '..' + ' '
            elif numero == '9':
                linha1 += '.*' + ' '
                linha2 += '*.' + ' '
                linha3 += '..' + ' '
            else: #numero == 0
                linha1 += '.*' + ' '
                linha2 += '**' + ' '
                linha3 += '..' + ' '
        print(linha1.strip())
        print(linha2.strip())
        print(linha3.strip())
    elif tipo == "B":
        celula1 = input().split()
        celula2 = input().split()
        celula3 = input().split()
        resposta = ''
        for i in range(len(celula1)):
            if celula1[i] + celula2[i] +celula3[i] == '*.....':
                resposta += '1'
            elif celula1[i] + celula2[i] +celula3[i] == '*.*...':
                resposta += '2'
            elif celula1[i] + celula2[i] +celula3[i] == '**....':
                resposta += '3'
            elif celula1[i] + celula2[i] +celula3[i] == '**.*..':
                resposta += '4'
            elif celula1[i] + celula2[i] +celula3[i] == '*..*..':
                resposta += '5'
            elif celula1[i] + celula2[i] +celula3[i] == '***...':
                resposta += '6'
            elif celula1[i] + celula2[i] +celula3[i] == '****..':
                resposta += '7'
            elif celula1[i] + celula2[i] +celula3[i] == '*.**..':
                resposta += '8'
            elif celula1[i] + celula2[i] +celula3[i] == '.**...':
                resposta += '9'
            elif celula1[i] + celula2[i] +celula3[i] == '.***..':
                resposta += '0'
        print(resposta)
    D = int(input())
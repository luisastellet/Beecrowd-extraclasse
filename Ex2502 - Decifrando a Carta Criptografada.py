#como sei se mudou o caso teste??

c, n = input().split()
c = int(c)
n = int(n)
#cifras maiusculas em string
cifra1max = input() 
cifra2max = input() 
#cifras minusculas em string
cifra1min = cifra1max.lower() 
cifra2min = cifra2max.lower()
#todas as cifras virando listas para comparar depois
cifra1max = list(cifra1max)
cifra2max = list(cifra2max)
cifra1min = list(cifra1min)
cifra2min = list(cifra2min)

for i in range(n):
    frase = input().split()

    # cada palavra separando em letras
    for i in range(len(frase)):
        frase[i] = list(frase[i])

    for y in range(len(frase)):
        for x in range(len(frase[y])):
            if frase[y][x] in cifra1min:
                posicao = cifra1min.index(frase[y][x])
                frase[y][x] = cifra2min[posicao]

            elif frase[y][x] in cifra1max:
                posicao = cifra1max.index(frase[y][x])
                frase[y][x] = cifra2max[posicao]

            elif frase[y][x] in cifra2min:
                posicao = cifra2min.index(frase[y][x])
                frase[y][x] = cifra1min[posicao]
            
            elif frase[y][x] in cifra2max:
                posicao = cifra2max.index(frase[y][x])
                frase[y][x] = cifra1max[posicao]
    
    #arrumando a resposta em string
    resp = ''
    for y in range(len(frase)):
        for x in frase[y]:
            resp += x
        resp += ' '

    print(resp.strip())
print()
while True:
    try:
        n = int(input("Enter a number: "))

        while n > 0:
            notas = list(map(int, input("Enter space-separated numbers: ").split()))
            soma = sum(notas)
            
            if soma % n == 0:
                media = soma // n
                resposta = 1 + sum([nota - media for nota in notas if nota >= media])
                print(resposta)
            else:
                print(-1)
            
            n = int(input("Enter a number: "))
    except:
        EOFError

N = int(input())
hora = N // 3600
resto = N - (hora * 3600)
minuto = resto // 60
resto -= minuto * 60
seg = resto
print(f"{hora}:{minuto}:{seg}")
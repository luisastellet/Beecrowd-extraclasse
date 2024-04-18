V = int(input())
teste = 1
while V != 0:
    cinquenta = V // 50
    resto = V % 50
    dez = resto // 10
    resto = resto % 10
    cinco = resto // 5
    resto = resto % 5
    um = resto // 1
    print(f"Teste {teste}")
    print(f'{cinquenta} {dez} {cinco} {um}')
    print()
    V = int(input())
    teste += 1
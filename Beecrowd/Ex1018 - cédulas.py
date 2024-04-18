N = int(input())

cem = N // 100
resto = N - (cem * 100)

cinquenta = resto // 50
resto -= cinquenta * 50

vinte = resto // 20
resto -= vinte * 20

dez = resto // 10
resto -= dez * 10

cinco = resto // 5
resto -= cinco * 5

dois = resto // 2
resto -= dois * 2

um = resto // 1

print(N)
print(f"{cem} nota(s) de R$ 100,00")
print(f"{cinquenta} nota(s) de R$ 50,00")
print(f"{vinte} nota(s) de R$ 20,00")
print(f"{dez} nota(s) de R$ 10,00")
print(f"{cinco} nota(s) de R$ 5,00")
print(f"{dois} nota(s) de R$ 2,00")
print(f"{um} nota(s) de R$ 1,00")

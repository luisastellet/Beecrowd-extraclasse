N = float(input())
inteiro = N // 1
decimal = N - inteiro
cem = inteiro // 100
resto = inteiro - (cem * 100)

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


print("NOTAS:")
print(f"{cem:.0f} nota(s) de R$ 100.00")
print(f"{cinquenta:.0f} nota(s) de R$ 50.00")
print(f"{vinte:.0f} nota(s) de R$ 20.00")
print(f"{dez:.0f} nota(s) de R$ 10.00")
print(f"{cinco:.0f} nota(s) de R$ 5.00")
print(f"{dois:.0f} nota(s) de R$ 2.00")


um = resto // 1

mcinquenta = decimal // 0.5
resto = decimal - (mcinquenta * 0.5)

mvintecinco = resto // 0.25
resto -= mvintecinco * 0.25

mdez = resto // 0.1
resto -= mdez * 0.1

mcinco = resto // 0.05
resto -= mcinco * 0.05
print(resto)
mum = resto / 0.01
print(mum)

print("MOEDAS:")
print(f"{um:.0f} moeda(s) de R$ 1.00")
print(f"{mcinquenta:.0f} moeda(s) de R$ 0.50")
print(f"{mvintecinco:.0f} moeda(s) de R$ 0.25")
print(f"{mdez:.0f} moeda(s) de R$ 0.10")
print(f"{mcinco:.0f} moeda(s) de R$ 0.05")
print(f"{mum:.0f} moeda(s) de R$ 0.01")

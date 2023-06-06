x = float(input())
if 0 <= x <= 400.00:
    percentual = 15
    ganho = 0.15*x
    salario = x + ganho
elif 400.01 <= x <= 800.00:
    percentual = 12
    ganho = 0.12*x
    salario = x + ganho
elif 800.01 <= x <= 1200.00:
    percentual = 10
    ganho = 0.10*x
    salario = x + ganho
elif 1200.01 <= x <= 2000.00:
    percentual = 7
    ganho = 0.07*x
    salario = x + ganho
else:
    percentual = 4
    ganho = 0.04*x
    salario = x + ganho

print(f"Novo salario: {salario:.2f}")
print(f"Reajuste ganho: {ganho:.2f}")
print(f"Em percentual: {percentual} %")
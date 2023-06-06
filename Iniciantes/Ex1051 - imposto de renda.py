x = float(input())
if 0 <= x <= 2000.00:
    print("Isento")
elif 2000.01 <= x <= 3000.00: #8%
    imposto = (x - 2000.00) * 0.08

elif 3000.01 <= x <= 4500.00: #18%
    imposto = ((x-3000)*0.18) + 80

elif x > 4500.0: #28%
    imposto = ((x-4500)*0.28) + 80 + 270

if x > 2000.00:
    print(f"R$ {imposto:.2f}")
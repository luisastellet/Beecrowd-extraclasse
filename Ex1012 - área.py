#Área
valores = list(map(float, input().split()))
A = float(valores[0])
B = float(valores[1])
C = float(valores[2])
tri = A * C / 2
cir = 3.14159 * C**2
tra = (A + B) * C / 2
qua = B**2
ret = A * B
print(f"TRIANGULO: {tri:.3f}")
print(f"CIRCULO: {cir:.3f}")
print(f"TRAPEZIO: {tra:.3f}")
print(f"QUADRADO: {qua:.3f}")
print(f"RETANGULO: {ret:.3f}")

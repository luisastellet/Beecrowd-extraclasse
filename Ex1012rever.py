#Área
valores = float(input())
lista = valores.split()
A = float(lista[0])
B = float(lista[1])
C = float(lista[2])
tri = A * C / 2
cir = 3.14159 * C**2
tra = (A + B) * C / 2
qua = B**2
ret = A * B
print("TRIANGULO:", tri)
print("CIRCULO:", cir)
print("TRAPEZIO:", tra)
print("QUADRADO:", qua)
print("RETÂNGULO:", ret)

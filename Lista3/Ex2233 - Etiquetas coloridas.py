R = int(input(), 16) #vermelho
G = int(input(), 16) #verde
B = int(input(), 16) #azul
quantR = 1
quantG = (R // G)**2
quantB = quantG * (G // B) **2
resultado = quantR + quantG + quantB
print(f"{resultado:x}")
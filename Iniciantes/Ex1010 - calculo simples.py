peca1 = input().split()
peca2 = input().split()
peca1[0] = int(peca1[0])
peca1[1] = int(peca1[1])
peca1[2] = float(peca1[2])

peca2[0] = int(peca2[0])
peca2[1] = int(peca2[1])
peca2[2] = float(peca2[2])
valor = (peca1[1] * peca1[2]) + (peca2[1] * peca2[2])

print(f"VALOR A PAGAR: R$ {valor:.2f}")


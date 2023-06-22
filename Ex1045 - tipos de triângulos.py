Ai, Bi, Ci = list(map(float, input().split()))
if Ai >= Bi and Ai >= Ci:
    A = Ai
    if Bi >= Ci:
        B = Bi
        C = Ci
    else:
        B = Ci
        C = Bi

elif Bi >= Ai and Bi >= Ci:
    A = Bi
    if A >= Ci:
        B = Ai
        C = Ci
    else:
        B = Ci
        C = Ai

elif Ci >= Ai and Ci >= Bi:
    A = Ci
    if A >= Bi:
        B = Ai
        C = Bi
    else:
        B = Bi
        C = Ai

if A >= (B + C):
    print("NAO FORMA TRIANGULO")
else:
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")

    if A**2 > (B**2 + C**2):
        print("TRIANGULO OBTUSANGULO")
    elif A**2 < (B**2 + C**2):
        print("TRIANGULO ACUTANGULO")

    if A == B == C:
        print("TRIANGULO EQUILATERO")
    if A == B != C or A == C != B or B == C != A:
        print("TRIANGULO ISOSCELES")
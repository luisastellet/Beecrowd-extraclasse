A, B, C = list(map(int,input().split()))
maior = A
if B > maior:
    maior = B
if C > maior:
    maior = C
print(f"{maior} eh o maior")

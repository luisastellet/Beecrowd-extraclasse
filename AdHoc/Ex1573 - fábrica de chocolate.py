import math
A,B,C = map(int,input().split())
while A != 0 or B != 0 or C != 0:
    volume = A*B*C
    #volume == a**3
    a = (volume)**(1/3)
    print(math.trunc(a))
    A, B, C = map(int, input().split())
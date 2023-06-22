X = int(input())
if X % 2 == 0: #par
    for c in range(X+1, X+12 , 2):
        if c % 2 != 0:
            print(c)
else: #ímpar
    for i in range(X, X + 11 , 2):
        if i % 2 != 0:
            print(i)
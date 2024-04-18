X0, Y0, X1, Y1 = map(int,input().split())
W0, Z0, W1, Z1 = map(int,input().split())
if X0 <= W0 <= X1 or X0 <= W1 <= X1 or W0 <= X0 <= W1 or W0 <= X1 <= W1:
    print('1')
elif Y0 <= Z0 <= Y1 or Y0 <= Z1 <= Y1 or Z0 <= Y0 <= Z1 or Z0 <= Y1 <= Z1:
    print('1')
else:
    print('0')

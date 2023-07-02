A,B,C,D = map(int,input().split())
n = A
while n < C:
    if n % A == 0 and n % B != 0 and C % n == 0 and D % n != 0:
        resp = n
        break
    else:
        resp = -1
    n += 1

if resp == -1:
    print(-1)
else:
    print(resp)

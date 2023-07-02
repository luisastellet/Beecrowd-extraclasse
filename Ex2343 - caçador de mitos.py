n = int(input())

coord = [[False] * 501 for _ in range(501)]

result = False

for _ in range(n):
    x, y = map(int, input().split())

    if coord[x][y]:
        result = True
        break

    coord[x][y] = True

if result:
    print("1")
else:
    print("0")


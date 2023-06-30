n,m = map(int,input().split())
chaves = list(map(int,input().split()))
mov = 0
for i in range(0, len(chaves)-1):
    if chaves[i] > m:
        mov += (chaves[i] - m)
        mudanca = chaves[i] - m
        chaves[i] -= mudanca
        chaves[i+1] -= mudanca
    elif chaves[i] < m:
        mov += (m - chaves[i])
        mudanca = m - chaves[i]
        chaves[i] += mudanca
        chaves[i+1] += mudanca
print(mov)
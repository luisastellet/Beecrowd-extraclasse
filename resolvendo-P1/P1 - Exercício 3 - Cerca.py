n, h = map(int,input().split())
alturas = list(map(int,input().split())) #n termos
mov = 0
for i in range(1, len(alturas)):
    if alturas[i-1] > h:
        mov += (alturas[i-1] - h)
        mudanca = (alturas[i-1] - h)
        alturas[i-1] -= (mudanca)
        alturas[i] -= (mudanca)

    elif alturas[i-1] < h:
        mov += (h - alturas[i-1])
        mudanca = (h - alturas[i-1])
        alturas[i-1] += (mudanca)
        alturas[i] += (mudanca)
print(mov)
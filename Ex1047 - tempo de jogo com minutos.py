hi, mi, hf, mf = list(map(int, input().split()))
hmi = hi * 60
hmf = hf * 60

if hf < hi:
    dhor = 24 - hi + hf
    if mf < mi:
        dmin = 60 - mi + mf
        dhor -= 1
    else:
        dmin = mf - mi
elif hi == hf:
    if mi < mf:
        dhor = 0
    else:
        dhor = 24
    if mf < mi:
        dmin = 60 - mi + mf
        dhor -= 1
    else:
        dmin = mf - mi
else: #hi < hf
    dhor = hf - hi
    if mf < mi:
        dmin = 60 - mi + mf
        dhor -=1
    else:
        dmin = mf - mi

print(f"O JOGO DUROU {dhor} HORA(S) E {dmin} MINUTO(S)")
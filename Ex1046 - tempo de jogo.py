hi, hf = list(map(int, input().split()))
if hf < hi:
    duracao = 24 - hi + hf
elif hi == hf:
    duracao = 24
else:
    duracao = hf - hi

print(f"O JOGO DUROU {duracao} HORA(S)")

pa,cb,pb,ca = input().split()
pA = list(map(int, pa.split(':')))
cB = list(map(int, cb.split(':')))
pB = list(map(int, pb.split(':')))
cA = list(map(int, ca.split(':')))

pa = pA[0] * 60 + pA[1]
cb = cB[0] * 60 + cB[1]
pb = pB[0] * 60 + pB[1]
ca = cA[0] * 60 + cA[1]


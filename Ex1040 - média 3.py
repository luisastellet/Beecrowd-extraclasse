n1, n2, n3, n4 = list(map(float, input().split()))
media = (n1*2 + n2*3 + n3*4 + n4)/10
if media >= 7.0:
    print(f"Media: {media:.1f}")
    print("Aluno aprovado.")
elif 5.0 <= media <= 6.9:
    print(f"Media: {media:.1f}")
    print("Aluno em exame.")
    nota = float(input())
    print(f"Nota do exame: {nota}")
    media = (nota + media) / 2
    if media >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media:.1f}")
else: #media < 5.0
    print(f"Media: {media:.1f}")
    print("Aluno reprovado.")
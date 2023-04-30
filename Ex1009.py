#Salário com Bônus
nome = input()
fixo = float(input())
vendas = float(input())
recebe = fixo + 0.15 * vendas
print("TOTAL = R$ {:.2f}" .format(recebe))
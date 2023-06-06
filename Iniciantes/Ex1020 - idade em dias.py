dias = int(input())
if dias >= 365:
    ano = dias // 365
    if dias - (ano * 365) >= 30:
        mes = (dias - (ano * 365)) // 30
    else:
        mes = 0
    if dias - (mes * 30) >= 0:
        dia = dias - (mes * 30) - (ano * 365)
    else:
        dia = 0
elif 365 > dias >= 30:
    ano = 0
    mes = dias // 30
    if dias - (mes * 30) >= 0:
        dia = dias - (mes * 30) - (ano * 365)
    else:
        dia = 0
else:
    ano = 0
    mes = 0
    dia = dias
print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{dia} dia(s)")
"""
Exercício 5 - Reajuste de Catálogo (Setor Comercial)
precos = {"cadeira": 350, "mesa": 700, "estante": 500}
Peça o percentual de reajuste e aplique a todos os produtos do dicionário.
"""

precos = {"cadeira": 350, "mesa": 700, "estante": 500}

perc_reajuste = input("Qual o percentual de reajuste? ")
perc_reajuste = float(perc_reajuste.replace("%", "")) / 100

for produto in precos:
    precos[produto] = precos[produto] * (1 + perc_reajuste)

print(precos)

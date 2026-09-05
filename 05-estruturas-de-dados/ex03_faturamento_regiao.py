"""
Exercício 3 - Faturamento por Região (Setor Financeiro)
vendas_regiao = {"Nordeste": 32000, "Sudeste": 58000, "Sul": 21000}
Extraia os valores, calcule o total e a média de faturamento.
"""

vendas_regiao = {"Nordeste": 32000, "Sudeste": 58000, "Sul": 21000}

valores = list(vendas_regiao.values())
total = sum(valores)
media = total / len(valores)

print("Total:", total)
print("Média:", media)

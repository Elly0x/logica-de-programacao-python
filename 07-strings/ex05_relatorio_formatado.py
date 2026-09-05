"""
Exercício 5 - Relatório de Custos (Setor Financeiro)
Um projeto teve receita de R$ 32.000,00 e custo de R$ 21.750,00. Calcule
o lucro e a margem (lucro / receita). Exiba o lucro com separador de
milhar e duas casas decimais, e a margem como porcentagem inteira.
"""

receita = 32000
custo = 21750

lucro = receita - custo
margem = lucro / receita

print(f"Lucro: R${lucro:,.2f}, Margem: {margem:.0%}")

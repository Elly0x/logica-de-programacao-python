"""
Exercício 2 - Comissão Progressiva por Venda (Setor de Vendas)
Dada a lista de vendas = [1800, 6200, 900, 4700, 3100], aplique 8% de
comissão para vendas acima de R$ 4.000,00 e 4% para as demais. Some e
exiba o total de comissão.
"""

vendas = [1800, 6200, 900, 4700, 3100]
comissao_total = 0

for venda in vendas:
    if venda > 4000:
        taxa = 0.08
    else:
        taxa = 0.04
    comissao_total += venda * taxa

print(f"Comissão total: R${comissao_total:,.2f}")

"""
Exercício 4 - Bônus por Meta Dupla (Setor Comercial)
Um bônus só é pago se as vendas do vendedor E as vendas da filial
baterem a meta. Vendedor: 4.500 (meta 4.000). Filial: 22.000
(meta 25.000). Calcule o bônus (15% das vendas do vendedor) ou zero.
"""

meta_vendedor = 4000
vendas_vendedor = 4500
meta_filial = 25000
vendas_filial = 22000

if vendas_vendedor >= meta_vendedor and vendas_filial >= meta_filial:
    bonus = vendas_vendedor * 0.15
else:
    bonus = 0

print(f"Bônus: R${bonus:,.2f}")

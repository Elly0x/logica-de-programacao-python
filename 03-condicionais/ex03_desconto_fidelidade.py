"""
Exercício 3 - Desconto por Fidelidade (Setor de Vendas)
Um programa de fidelidade aplica desconto conforme o valor da compra:
- A partir de R$ 300,00: 12% de desconto
- A partir de R$ 100,00 (e menos de 300): 5% de desconto
- Abaixo de R$ 100,00: sem desconto
Calcule e exiba o valor final formatado em reais.
"""

valor_compra = 250

if valor_compra < 100:
    perc_desconto = 0
elif valor_compra < 300:
    perc_desconto = 0.05
else:
    perc_desconto = 0.12

desconto = valor_compra * perc_desconto
valor_final = valor_compra - desconto

print(f"Desconto: R${desconto:,.2f}. Valor final: R${valor_final:,.2f}")

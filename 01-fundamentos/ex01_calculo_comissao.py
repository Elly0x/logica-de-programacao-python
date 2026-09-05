"""
Exercício 1 - Cálculo de Comissão (Setor de Vendas)
Uma vendedora fechou um contrato de R$ 8.200,00. A empresa paga comissão
de 12% sobre o valor do contrato. Calcule o valor da comissão e o valor
que a empresa recebe líquido (contrato - comissão).
"""

valor_contrato = 8200
perc_comissao = 0.12

comissao = valor_contrato * perc_comissao
valor_liquido = valor_contrato - comissao

print("Comissão:", comissao)
print("Valor líquido para a empresa:", valor_liquido)

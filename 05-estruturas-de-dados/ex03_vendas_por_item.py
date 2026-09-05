"""
Exercício 3 - Processamento de Vendas por Item (Setor Comercial)
vendas_dia = [("Caderno", 12, 30), ("Caneta", 3, 100), ("Mochila", 90, 5)]
Cada tupla é (produto, preco_unitario, quantidade). Some o total por item.
"""

vendas_dia = [("Caderno", 12, 30), ("Caneta", 3, 100), ("Mochila", 90, 5)]

for produto, preco, qtde in vendas_dia:
    total = preco * qtde
    print(f"{produto}: R${total}")

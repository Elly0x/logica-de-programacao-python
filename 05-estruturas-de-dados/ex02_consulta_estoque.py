"""
Exercício 2 - Consulta de Estoque (Setor de Logística)
estoque = {"parafuso": 300, "porca": 450, "arruela": 120}
Peça o nome do produto e exiba a quantidade, ou uma mensagem de "não
encontrado" caso não exista.
"""

estoque = {"parafuso": 300, "porca": 450, "arruela": 120}

produto = input("Digite o nome do produto: ")
produto = produto.strip().lower()

if produto in estoque:
    print(f"{produto}: {estoque[produto]} unidades")
else:
    print("Produto não encontrado no sistema")

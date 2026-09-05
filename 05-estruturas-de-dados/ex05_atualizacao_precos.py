"""
Exercício 5 - Atualização Interativa de Preços (Setor de Estoque)
produtos = ["Camiseta", "Calça", "Boné"]
precos = [59.9, 129.9, 39.9]
Peça o nome do produto e o novo preço, e atualize a lista correspondente.
"""

produtos = ["Camiseta", "Calça", "Boné"]
precos = [59.9, 129.9, 39.9]

produto_escolhido = input("Digite o produto a ser alterado: ")
novo_preco = input("Novo preço: ")
novo_preco = float(novo_preco.replace("R$", "").replace(",", "."))

posicao = produtos.index(produto_escolhido)
precos[posicao] = novo_preco

print(produtos)
print(precos)

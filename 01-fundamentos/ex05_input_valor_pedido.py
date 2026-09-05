"""
Exercício 5 - Leitura de Valor de Pedido (Setor de Vendas)
Peça ao usuário o valor de um pedido, tratando o texto caso venha com "R$"
e vírgula decimal, converta para float e exiba o valor com duas casas
decimais formatado em reais.
"""

valor = input("Digite o valor do pedido: ")
valor = valor.replace("R$", "").replace(".", "").replace(",", ".")
valor_numerico = float(valor)

print(f"Valor do pedido: R${valor_numerico:,.2f}")

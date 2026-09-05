"""
Exercício 1 - Classificação de Cliente (Setor de Vendas)
Peça o valor total de compras de um cliente no ano.
- Menor que R$ 2.000,00: "Cliente Bronze"
- Entre R$ 2.000,00 e R$ 10.000,00 (inclusive): "Cliente Prata"
- Acima de R$ 10.000,00: "Cliente Ouro"
"""

valor = input("Digite o total de compras do cliente: ")
valor = valor.replace("R$", "").replace(".", "").replace(",", ".")
valor = float(valor)

if valor < 2000:
    print("Cliente Bronze")
elif valor <= 10000:
    print("Cliente Prata")
else:
    print("Cliente Ouro")

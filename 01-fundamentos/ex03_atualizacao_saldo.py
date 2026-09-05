"""
Exercício 3 - Atualização de Saldo (Setor Financeiro)
Uma conta empresarial começa o mês com saldo de R$ 12.000,00. Durante o mês,
houve uma saída de R$ 4.500,00 (fornecedores) e uma entrada de R$ 7.300,00
(clientes). Atualize e exiba o saldo final.
"""

saldo = 12000
saida = 4500
entrada = 7300

saldo = saldo - saida + entrada

print("Saldo final:", saldo)

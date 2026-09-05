"""
Exercício 2 - Cálculo de Folha (Setor de RH)
Crie uma função calcular_folha que receba o salário bruto e retorne o
desconto (8%) e o salário líquido. Chame para um salário de R$ 3.800,00.
"""

def calcular_folha(salario):
    desconto = salario * 0.08
    liquido = salario - desconto
    return desconto, liquido

salario = 3800
desconto, liquido = calcular_folha(salario)

print(f"Desconto: R${desconto:,.2f} | Líquido: R${liquido:,.2f}")

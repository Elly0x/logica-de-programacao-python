"""
Exercício 2 - Calculadora de Frete (Setor de Logística)
Crie a função calcular_frete que receba o peso do pacote.
- Acima de 10kg: taxa de R$ 3,50 por kg
- Até 10kg: taxa de R$ 2,00 por kg
Retorne o valor do frete. Teste com 15kg e 6kg.
"""

def calcular_frete(peso):
    if peso > 10:
        taxa = 3.50
    else:
        taxa = 2.00
    return peso * taxa

print(calcular_frete(15))
print(calcular_frete(6))

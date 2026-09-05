"""
Exercício 1 - Relatório de Produção Diária (Setor de Fábrica)
producao = [320, 410, 290, 500, 380]
Exiba o total produzido na semana, a média diária, o melhor e o pior dia.
"""

producao = [320, 410, 290, 500, 380]

total = sum(producao)
media = total / len(producao)
melhor_dia = max(producao)
pior_dia = min(producao)

print(f"Total: {total}, Média: {media}, Melhor: {melhor_dia}, Pior: {pior_dia}")

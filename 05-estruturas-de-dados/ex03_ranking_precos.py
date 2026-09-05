"""
Exercício 3 - Ranking de Preços (Setor Comercial)
precos = [45, 120, 30, 200, 75]
Ordene do maior para o menor e monte uma lista top_3 com os 3 maiores.
"""

precos = [45, 120, 30, 200, 75]

precos.sort(reverse=True)
top_3 = precos[:3]

print(precos)
print(top_3)

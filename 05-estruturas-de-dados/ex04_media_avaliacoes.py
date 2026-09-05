"""
Exercício 4 - Média de Avaliações de Atendimento (Setor de CX)
avaliacoes = {"Suporte A": [9, 8, 10], "Suporte B": [6, 7, 5]}
Peça o nome da equipe e calcule a média das notas dela.
"""

avaliacoes = {"Suporte A": [9, 8, 10], "Suporte B": [6, 7, 5]}

equipe = input("Digite o nome da equipe: ")
notas = avaliacoes[equipe]
media = sum(notas) / len(notas)

print(f"A média de {equipe} foi {media}")

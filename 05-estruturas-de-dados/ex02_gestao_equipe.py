"""
Exercício 2 - Gestão de Equipe (Setor de RH)
equipe = ["Ana", "Bruno", "Carlos", "Diego"]
1. Adicionar "Elaine" ao final.
2. "Bruno" foi promovido, atualize para "Bruno (Sênior)".
3. Verificar se "Fabio" está na equipe.
4. Remover "Carlos", que saiu da empresa.
"""

equipe = ["Ana", "Bruno", "Carlos", "Diego"]

equipe.append("Elaine")

posicao_bruno = equipe.index("Bruno")
equipe[posicao_bruno] = "Bruno (Sênior)"

fabio_na_equipe = "Fabio" in equipe
print("Fabio está na equipe?", fabio_na_equipe)

equipe.remove("Carlos")
print(equipe)

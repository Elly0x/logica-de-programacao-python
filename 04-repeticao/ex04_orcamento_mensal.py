"""
Exercício 4 - Comparação de Orçamento Mensal (Setor Financeiro)
metas = {"abr": 800, "mai": 950, "jun": 1000}
gastos = {"abr": 750, "mai": 1100, "jun": 1000}
Percorra os meses informando se o orçamento foi respeitado ou estourado
(e por quanto).
"""

metas = {"abr": 800, "mai": 950, "jun": 1000}
gastos = {"abr": 750, "mai": 1100, "jun": 1000}

for mes in gastos:
    if gastos[mes] > metas[mes]:
        diferenca = gastos[mes] - metas[mes]
        print(f"Mês {mes}: orçamento estourado em R${diferenca}")
    else:
        print(f"Mês {mes}: dentro do orçamento")

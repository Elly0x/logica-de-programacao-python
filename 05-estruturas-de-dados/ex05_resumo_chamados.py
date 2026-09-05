"""
Exercício 5 - Resumo de Chamados (Setor de TI)
Crie uma função resumo_chamados que receba tempos de espera (minutos) e
retorne a quantidade de chamados e o tempo máximo. Teste com
tempos = [22, 8, 60, 15].
"""

def resumo_chamados(tempos):
    quantidade = len(tempos)
    maximo = max(tempos)
    return quantidade, maximo

tempos = [22, 8, 60, 15]
quantidade, maximo = resumo_chamados(tempos)

print(f"Foram abertos {quantidade} chamados. Tempo máximo: {maximo} min")

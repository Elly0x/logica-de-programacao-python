"""
Exercício 4 - Performance de Filiais (Setor de Dashboard)
Crie uma função analisar_vendas que retorna total e média de uma lista.
dados_filiais = {"Central": [8000, 9500], "Norte": [4000, 6000, 5500]}
Percorra o dicionário e desempacote o resultado da função para cada filial.
"""

def analisar_vendas(lista_vendas):
    total = sum(lista_vendas)
    media = total / len(lista_vendas)
    return total, media

dados_filiais = {"Central": [8000, 9500], "Norte": [4000, 6000, 5500]}

for filial in dados_filiais:
    total, media = analisar_vendas(dados_filiais[filial])
    print(f"Filial {filial} -> Total: R${total}, Média: R${media}")

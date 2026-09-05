"""
Exercício 4 - Verificador de Meta de Vendedores (Setor Comercial)
Crie a função quem_bateu_meta que receba um dicionário de vendedores e a
meta, imprimindo quem atingiu ou superou o valor.
"""

def quem_bateu_meta(vendedores, meta):
    for vendedor in vendedores:
        if vendedores[vendedor] >= meta:
            print(f"{vendedor} bateu a meta!")

equipe = {"Tais": 9000, "Bruno": 12500, "Igor": 7000}
meta = 8000

quem_bateu_meta(equipe, meta)

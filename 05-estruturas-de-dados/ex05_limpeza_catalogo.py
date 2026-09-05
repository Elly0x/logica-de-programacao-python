"""
Exercício 5 - Limpeza de Catálogo (Setor de TI)
produtos = {"tablet": 900, "smartwatch": 400, "fita_cassete": 30, "fone": 150}
Remova "fita_cassete" (descontinuado), exiba o valor removido e verifique
se "tablet" ainda existe.
"""

produtos = {"tablet": 900, "smartwatch": 400, "fita_cassete": 30, "fone": 150}

preco_removido = produtos.pop("fita_cassete")
print("Removido:", "fita_cassete", "-", preco_removido)

tablet_existe = "tablet" in produtos
print("Tablet no catálogo?", tablet_existe)

"""
Exercício 3 - Verificação de Estoque Crítico (Setor de Logística)
Dadas as listas produtos = ["cabo", "fone", "carregador", "capinha"] e
quantidades = [3, 15, 6, 20], com estoque mínimo de 10 unidades, alerte
sobre os produtos abaixo do mínimo.
"""

produtos = ["cabo", "fone", "carregador", "capinha"]
quantidades = [3, 15, 6, 20]

for i, quantidade in enumerate(quantidades):
    if quantidade < 10:
        produto = produtos[i]
        print(f"ALERTA: {produto} está com apenas {quantidade} unidades")

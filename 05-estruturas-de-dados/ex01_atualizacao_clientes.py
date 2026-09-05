"""
Exercício 1 - Atualização de Faturamento de Clientes (Setor de CRM)
clientes = {"Bia": 4200, "Otto": 2100, "Renata": 3800}
"Otto" fez uma nova compra de R$ 900,00. Atualize, adicione um novo
cliente "Sergio" com R$ 1.500,00 e exiba o dicionário atualizado.
"""

clientes = {"Bia": 4200, "Otto": 2100, "Renata": 3800}

clientes["Otto"] += 900
clientes["Sergio"] = 1500

print(clientes)

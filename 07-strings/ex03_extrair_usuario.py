"""
Exercício 3 - Extração de Usuário de Log (Setor de Segurança)
Dado o e-mail rafael.mendes@novatech.com, extraia apenas a parte antes
do "@" usando .find() e fatiamento.
"""

email = "rafael.mendes@novatech.com"

posicao_arroba = email.find("@")
usuario = email[:posicao_arroba]

print(usuario)

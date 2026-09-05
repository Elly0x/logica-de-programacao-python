"""
Exercício 2 - Migração de Domínio de E-mail (Setor de TI)
A empresa "TechCorp" foi renomeada para "NovaTech". O e-mail
carla_souza@techcorp.com.br precisa passar a usar o domínio
@novatech.com. Faça a substituição automaticamente.
"""

email = "carla_souza@techcorp.com.br"
novo_dominio = "@novatech.com"

email = email.replace("@techcorp.com.br", novo_dominio)

print(email)

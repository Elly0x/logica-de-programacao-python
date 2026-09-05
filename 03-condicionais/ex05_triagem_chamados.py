"""
Exercício 5 - Triagem de Chamados de Suporte (Setor de TI)
Peça o assunto de um chamado. Se contiver "senha" ou "acesso", encaminhe
para "Segurança". Se contiver "lentidão" ou "travando", encaminhe para
"Infraestrutura". Caso contrário, encaminhe para "Suporte Geral".
"""

assunto = input("Digite o assunto do chamado: ")
assunto = assunto.lower()

if "senha" in assunto or "acesso" in assunto:
    print("Encaminhado para Segurança")
elif "lentidão" in assunto or "travando" in assunto:
    print("Encaminhado para Infraestrutura")
else:
    print("Encaminhado para Suporte Geral")

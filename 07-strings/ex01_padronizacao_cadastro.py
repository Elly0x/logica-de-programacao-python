"""
Exercício 1 - Padronização de Cadastro (Setor de CRM)
Um cliente foi cadastrado como: nome = "  fernanda lima souza  " e
email = "  FERNANDA.LIMA@OUTLOOK.COM  ". Remova espaços extras, deixe o
nome em formato de título e o email em minúsculas.
"""

nome = "  fernanda lima souza  "
email = "  FERNANDA.LIMA@OUTLOOK.COM  "

nome = nome.strip().title()
email = email.strip().lower()

print(nome)
print(email)

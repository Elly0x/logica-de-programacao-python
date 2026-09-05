"""
Exercício 2 - Controle de Login (Setor de Segurança)
Uma lista de e-mails autorizados: autorizados = ["joao@empresa.com",
"lia@empresa.com"]. Peça o e-mail do usuário, padronize e verifique se
está na lista, exibindo "Acesso permitido" ou "Acesso negado".
"""

autorizados = ["joao@empresa.com", "lia@empresa.com"]

email = input("Digite seu e-mail: ")
email = email.strip().lower()

if email in autorizados:
    print("Acesso permitido")
else:
    print("Acesso negado")

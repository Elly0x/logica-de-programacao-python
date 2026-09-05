"""
Exercício 4 - Saudação Personalizada (Setor de Marketing)
Dado o nome completo "mariana costa albuquerque", extraia o primeiro
nome, capitalize a primeira letra e monte a mensagem
"Olá, [Primeiro Nome], tudo bem?".
"""

mensagem = "Olá, [Primeiro Nome], tudo bem?"
nome = "mariana costa albuquerque"

posicao_espaco = nome.find(" ")
primeiro_nome = nome[:posicao_espaco].capitalize()

mensagem = mensagem.replace("[Primeiro Nome]", primeiro_nome)

print(mensagem)

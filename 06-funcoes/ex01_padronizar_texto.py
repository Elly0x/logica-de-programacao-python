"""
Exercício 1 - Padronizador de Nomes (Setor de E-commerce)
Crie a função padronizar_texto que remova espaços extras e formate em
título. Teste com uma lista de nomes bagunçados.
"""

produtos_baguncados = [" tenis nike ", "CAMISA POLO ", " mOcHiLa EsCoLaR"]

def padronizar_texto(texto):
    texto = texto.strip()
    texto = texto.title()
    return texto

produtos_padronizados = [padronizar_texto(p) for p in produtos_baguncados]

print(produtos_padronizados)

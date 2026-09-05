"""
Exercício 5 - Conversor de Moeda (Setor de Importação)
Crie converter_para_real e processar_lista_precos, que aplica a
conversão a uma lista de preços em dólar.
"""

def converter_para_real(valor_dolar, cotacao):
    return valor_dolar * cotacao

def processar_lista_precos(precos_dolar, cotacao):
    for preco in precos_dolar:
        preco_real = converter_para_real(preco, cotacao)
        print(f"US${preco} -> R${preco_real:,.2f}")

precos_usd = [80, 20, 150]
cotacao_dolar = 5.35

processar_lista_precos(precos_usd, cotacao_dolar)

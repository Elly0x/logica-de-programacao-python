"""
Exercício 3 - Analisador de Ocupação (Setor de Eventos)
Crie a função analisar_ocupacao que receba o número de presentes e a
capacidade do salão. Se ocupação >= 80%, retorne "Lotação Alta". Caso
contrário, "Lotação Normal".
"""

def analisar_ocupacao(presentes, capacidade):
    ocupacao = presentes / capacidade
    if ocupacao >= 0.8:
        return "Lotação Alta"
    else:
        return "Lotação Normal"

print(analisar_ocupacao(190, 200))

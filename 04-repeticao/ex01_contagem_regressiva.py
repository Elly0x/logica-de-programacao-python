"""
Exercício 1 - Contagem Regressiva de Envio (Setor de Logística)
Simule uma contagem regressiva de 8 avisos exibindo:
"Faltam X minutos para o carregamento do caminhão".
"""

for i in range(8):
    tempo_restante = 8 - i
    print(f"Faltam {tempo_restante} minutos para o carregamento do caminhão")

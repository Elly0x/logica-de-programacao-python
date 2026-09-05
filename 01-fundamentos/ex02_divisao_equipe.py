"""
Exercício 2 - Divisão de Equipe em Turnos (Setor de RH)
Uma fábrica tem 37 funcionários para dividir em turnos de 8 pessoas cada.
Calcule quantos turnos completos serão formados (//) e quantos funcionários
sobram para um turno extra (%).
"""

funcionarios = 37
tamanho_turno = 8

turnos_completos = funcionarios // tamanho_turno
funcionarios_restantes = funcionarios % tamanho_turno

print("Turnos completos:", turnos_completos)
print("Funcionários no turno extra:", funcionarios_restantes)

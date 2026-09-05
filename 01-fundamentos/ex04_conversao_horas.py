"""
Exercício 4 - Conversão de Horas Trabalhadas (Setor de RH)
Um funcionário registrou 130 horas de trabalho no mês. Converta esse valor
para o formato "X dias e Y horas", considerando uma jornada de 8 horas por dia.
"""

total_horas = 130
horas_por_dia = 8

dias = total_horas // horas_por_dia
horas_restantes = total_horas % horas_por_dia

print(f"O funcionário trabalhou {dias} dias e {horas_restantes} horas")

"""
Exercício 4 - Rota de Entregas (Setor de Logística)
rota = ["Recife", "Olinda", "Paulista"]
novas_cidades = ["Cabo", "Ipojuca"]
Junte as listas, descubra a posição de "Paulista" e monte a mensagem
"Paulista é a Xª cidade da rota".
"""

rota = ["Recife", "Olinda", "Paulista"]
novas_cidades = ["Cabo", "Ipojuca"]

rota.extend(novas_cidades)

posicao_paulista = rota.index("Paulista") + 1

print(rota)
print(f"Paulista é a {posicao_paulista}ª cidade da rota")

import utilidades
import random
import datetime

print(utilidades.linha("="))
print("SORTEIO DE BRINDES - FEIRA DE CIÊNCIAS")
print(utilidades.linha("="))

participantes = []

print("Digite os nomes dos participantes (Enter para terminar).")

contador = 1

while True:

    nome = utilidades.ler_texto(
        f"Participante {contador}: ",
        vazio=True
    )

    if nome == "":
        break

    if nome.lower() in [i.lower() for i in participantes]:
        print(f"{nome} já está na lista.")
    else:
        participantes.append(nome)
        contador += 1

if len(participantes) == 0:
    print("Nenhum participante cadastrado.")
    exit()

quantidade_brindes = utilidades.ler_inteiro(f"Quantos brindes (1 a {len(participantes)})? ", 1, len(participantes))

brindes = []

for i in range(quantidade_brindes):

    nome_brinde = utilidades.ler_texto(f"Brinde {i + 1}: ")

    brindes.append(nome_brinde)

ganhadores = random.sample(participantes, quantidade_brindes)

data_hora = datetime.datetime.now().strftime("%d/%m/%Y às %H:%M")

print(utilidades.linha("-"))

print(f"Sorteio realizado em {data_hora}")
print(f"{len(participantes)} participantes, {quantidade_brindes} brindes")

print(utilidades.linha("-"))

for i in range(quantidade_brindes):

    print(f"{brindes[i]} -> {ganhadores[i]}")

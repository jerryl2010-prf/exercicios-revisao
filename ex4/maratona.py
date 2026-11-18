

def formatar_duracao(minutos):
    horas = minutos // 60
    minutos_restantes = minutos % 60

    if horas > 0:
        return f"{horas}h{minutos_restantes:02d}min"
    else:
        return f"{minutos}min"


def tempo_total(duracoes):
    total = 0

    for duracao in duracoes:
        total += duracao

    return total


def dias_para_terminar(total_minutos, minutos_por_dia=120):
    return (total_minutos + minutos_por_dia - 1) // minutos_por_dia


def classificar_maratona(total_minutos):
    if total_minutos < 300:
        return "Leve"
    elif total_minutos <= 900:
        return "Média"
    else:
        return "Intensa"

print("=== MARATONA DE SÉRIE ===")

nome = input("Nome da série: ")

while True:
    try:
        temporadas = int(input("Número de temporadas: "))

        if temporadas > 0:
            break
        else:
            print("Digite um número maior que zero!")

    except ValueError:
        print("Digite um número inteiro válido!")

duracoes_temporadas = []
total_geral = 0

for i in range(temporadas):

    print(f"\n--- Temporada {i + 1} ---")

    while True:
        try:
            episodios = int(input("Número de episódios: "))

            if episodios > 0:
                break
            else:
                print("Digite um número maior que zero!")

        except ValueError:
            print("Digite um número inteiro válido!")

    while True:
        try:
            duracao_media = int(input("Duração média de cada episódio (min): "))

            if duracao_media > 0:
                break
            else:
                print("A duração deve ser maior que zero!")

        except ValueError:
            print("Digite um número inteiro válido!")

    duracao_temporada = episodios * duracao_media

    duracoes_temporadas.append(duracao_temporada)

    print(f"Tempo da temporada: {formatar_duracao(duracao_temporada)}")

total_geral = tempo_total(duracoes_temporadas)

classificacao = classificar_maratona(total_geral)

dias_geral = dias_para_terminar(total_geral)

print(f"=== {nome.upper()} ===")

print(f"Série: {nome}")

for i in range(temporadas):
    print(f"Temporada {i + 1}: {formatar_duracao(duracoes_temporadas[i])}")

print(f"Tempo total: {formatar_duracao(total_geral)}")
print(f"Classificação: {classificacao}")

try:
    while True:
        tempo = int(input("Quanto tempo diariamente se dedica para assistir (min)? "))
        if tempo > 0:
            break
        else:
            print("Digite um número válido!")
except ValueError:
    print("Digite um número!")

dias_expetativa = dias_para_terminar(total_geral, tempo)

print(f"Você termina {nome} em {dias_expetativa} dias.")
print(f"Com 2 horas por dia (padrão), seria {dias_geral} dias.")


itens = []
pesos = []

peso_total = 0

while True:
    nome = input("Nome do item ou FIM para encerrar: ")

    if nome.lower() == "fim":
        break

    while True:
        try:
            peso = float(input("Peso do item (kg): ").replace(",", "."))
            if peso <= 0:
                print("O peso deve ser maior que zero!")
            else:
                break
        except ValueError:
            print("Peso inválido! Digite um número.")

    itens.append(nome)
    pesos.append(peso)
    peso_total += peso

    if peso_total > 15:
        print(f"O peso total passou de 15 kg! Está em {peso_total}Kg!")

if len(itens) == 0:
    print("A mochila está vazia.")

else:

    peso_medio = peso_total/len(itens)
    indice_mais_pesado = pesos.index(max(pesos))

    print("\n=== RESUMO ===")

    for i in range(len(itens)):
        print(f"{i + 1}. {itens[i]} - {pesos[i]:.2f}Kg")

    print(f"Quantidade de itens: {len(itens)}")
    print(f"Peso total: {peso_total:.2f}Kg")
    print(f"Peso médio: {peso_medio:.2f}Kg")

    print(f"Item mais pesado: {itens[indice_mais_pesado]} "
          f"({pesos[indice_mais_pesado]:.2f}Kg)")

    if peso_total > 15:
        print(f"É preciso tirar {peso_total - 15:.2f}Kg da mochila.")
    else:
        print(f"Ainda cabem {15 - peso_total:.2f}Kg na mochila.")
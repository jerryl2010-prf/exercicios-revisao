def subtotal_item(preco, quantidade=1):
    return preco * quantidade

def aplicar_cupom(total, cupom):
    cupom = "".join(cupom.upper().split())
    cupons = {"PROMO10": 0.9, "VOLTASAULAS": 0.85, "BLACK25": 0.75}
    novo_total = total
    percentual = 0
    mensagem = "Cupom inválido!"

    for cupon in cupons:
        if cupom == cupon:
            novo_total = total * cupons[cupon]
            percentual = round((1 - cupons[cupon]) * 100)
            mensagem = "Cupom validado!"
            break

    print(mensagem)
    return novo_total, percentual


def calcular_frete(total, gratis_acima=200.0, valor=25.0):
    if total >= gratis_acima:
        return 0
    else:
        return valor


def valor_parcela(total, parcelas=1):
    if parcelas <= 6:
        return total / parcelas
    else:
        return (total * (1 + 0.02 * parcelas)) / parcelas


carrinho = 0.0

print("=== CARRINHO DA LOJA ===")

while True:

    produto = input("Nome do produto (Enter para finalizar): ")

    if produto == "":
        break

    while True:
        try:
            preco = float(input("Preço do produto: R$ "))

            if preco <= 0:
                print("O preço deve ser maior que zero!")
            else:
                break

        except ValueError:
            print("Digite um preço válido!")

    while True:
        try:
            quantidade = int(input("Quantidade: "))

            if quantidade <= 0:
                print("A quantidade deve ser maior que zero!")
            else:
                break

        except ValueError:
            print("Digite uma quantidade válida!")

    subtotal = subtotal_item(preco, quantidade)

    carrinho += subtotal

    print(f"Subtotal de {produto}: R$ {subtotal:.2f}")
    print(f"Total do carrinho: R$ {carrinho:.2f}")


cupom = input("\nDigite o cupom de desconto (ou Enter para pular): ")

total_desconto, percentual = aplicar_cupom(carrinho, cupom)

desconto = carrinho - total_desconto

frete = calcular_frete(total_desconto)

total_final = total_desconto + frete

while True:
    try:
        parcelas = int(input("Número de parcelas (1 a 12): "))

        if 1 <= parcelas <= 12:
            break
        else:
            print("Escolha entre 1 e 12 parcelas!")

    except ValueError:
        print("Digite um número inteiro válido!")


valor_cada_parcela = valor_parcela(total_final, parcelas)

print("\n=== NOTA FISCAL ===")

print(f"Subtotal: R$ {carrinho:.2f}")
print(f"Desconto ({percentual}%): R$ {desconto:.2f}")
print(f"Frete: R$ {frete:.2f}")
print(f"Total: R$ {total_final:.2f}")

print(f"Parcelamento: {parcelas}x de R$ {valor_cada_parcela:.2f}")


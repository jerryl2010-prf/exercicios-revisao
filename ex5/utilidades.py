def ler_texto(mensagem, vazio=False):
    while True:
        texto = input(mensagem).strip()

        if vazio or texto != "":
            return texto

        print("O texto não pode ficar vazio!")

def ler_inteiro(mensagem, minimo=None, maximo=None):
    while True:
        try:
            numero = int(input(mensagem))

            if minimo is not None and numero < minimo:
                print(f"O mínimo é {minimo}.")
            elif maximo is not None and numero > maximo:
                print(f"O máximo é {maximo}.")
            else:
                return numero

        except ValueError:
            print("Digite um número inteiro válido!")


def linha(caractere="-", tamanho=40):
    return caractere * tamanho
total_turmas_viagem = []

while True:

    try:
        turmas = int(input("Quantas turmas vão participar? "))
        if turmas <= 0:
            print("Digite um número de turmas maior que 0!")
        else:
            break
    except ValueError:
        print("Digite um número inteiro maior que 0!")

for i in range(turmas):

    nome_turma = input("Digite o nome da turma: ")
    while True:

        try:
            num_alunos = int(input("Digite o número de alunos: "))
            if num_alunos < 0:
                print("O número de alunos deve ser maior que 0.")
            else:
                break
        except ValueError:
            print("Digite um valor válido!")

    sala = {"nome": nome_turma, "alunos": num_alunos}
    total_turmas_viagem.append(sala)

total_alunos = sum(sala['alunos'] for sala in total_turmas_viagem)

professores = (total_alunos + 14)//15

onibus = (total_alunos + professores + 43)//44

sobraram = (onibus*44) - (total_alunos + professores)

custo = onibus*1800

custo_aluno = custo/total_alunos

maior_sala_num = -1

maior_sala_nome = ""

for sala in total_turmas_viagem:
    if sala['alunos'] > maior_sala_num:
        maior_sala_num = sala['alunos']
        maior_sala_nome = sala['nome']

print(f"=== Resumo ===\nAlunos: {total_alunos}\nProfessores acompanhantes: {professores}\nTotal de pessoas: {total_alunos+professores}\nÔnibus necessários: {onibus} (Sobraram {sobraram} lugares)\nCusto total: R${custo}\nCusto por aluno: R${custo_aluno:.2f}\nTurma com mais alunos: {maior_sala_nome} com {maior_sala_num} alunos")


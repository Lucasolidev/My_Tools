# Programa - Controle de uma agenda de telefones

agenda = []

# Variável para marcar uma alteração na agenda
alterada = False


def pede_nome():
    return input("Qual Nome: ")


def pede_telefone():
    return input("Qual Telefone: ")


def mostra_dados(nome, telefone):
    print(f"-Nome: {nome} Telefone: {telefone}")


def pede_nome_arquivo():
    return input("Nome do Arquivo: ")


def pesquisa(nome):
    nome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == nome:
            return p
    return None


def novo():
    global agenda
    nome = pede_nome().title()
    telefone = pede_telefone()
    agenda.append([nome, telefone])


def confirma(operacao):
    while True:
        opcao = input(f"Confirmar {operacao} (S/N)?").upper()
        if opcao in "SN":
            return opcao
        else:
            print("Opcão inválida. Escolha S ou N.")


def apaga():
    global agenda
    nome = pede_nome()
    p = pesquisa(nome)
    if p is not None:
        del agenda[p]
        print("Não esqueça de salvar.")
    else:
        print("Nome não encontrado.")


def altera():
    p = pesquisa(pede_nome())
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print("Telefone Encontrado:")
        mostra_dados(nome, telefone)
        nome = pede_nome().title()
        telefone = pede_telefone()
        if confirma("alteração") == "S":
            agenda[p] = [nome, telefone]
            print("Telefone salvo na agenda.")
        else:
            print("Não foi salvo na agenda.")
    else:
        print("Nome não encontrado.")


def lista():
    print("\nAgenda\n\n------")
    # Usamos a função enumerate para obter a posição na agenda
    for posicao, e in enumerate(agenda):
        # Imprimimos a posição, sem saltar linha
        print(f"Posição: {posicao}", end="")
        mostra_dados(e[0], e[1])
    print("------\n")


def le():
    global agenda
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        agenda = []
        for l in arquivo.readlines():
            nome, telefone = l.strip().split("#")
            agenda.append([nome, telefone])
        print("Agenda lida com sucesso!")


def grava():
    global alterada
    if not alterada:
        print("Você não alterou a lista. Deseja gravá-la mesmo assim")
        if confirma("gravação") == "N":
            return
    print("Gravar\n------")
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for e in agenda:
            arquivo.write(f"{e[0]}#{e[1]}\n")
            arquivo.close()
            alterada = False


def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print("valor inválido, favor digitar entre {inicio} e {fim}")


def menu():
    print("""
    \n     Agenda\n
    1 - Novo
    2 - Alterar
    3 - Apagar
    4 - Listar
    5 - Salvar
    6 - Ler Arquivo
    7 - Ordena por nome

    0 - Sair
    """)
    print(f"\nNomes na agenda: {len(agenda)}\n")
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 6)


while True:
    opcao = menu()
    if opcao == 0:
        break
    if opcao == 1:
        novo()
    elif opcao == 2:
        altera()
    elif opcao == 3:
        apaga()
    elif opcao == 4:
        lista()
    elif opcao == 5:
        grava()
    elif opcao == 6:
        le()

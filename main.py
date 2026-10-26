# Leitura sequencial do arquivo CSV
funcionarios_processados = []
custo_total = 0.0

with open("dados.csv", "r", encoding="utf-8") as arquivo:
    cabecalho = arquivo.readline()
    print(cabecalho, end="")

    while True:
        linha = arquivo.readline()
        if linha == "":
            break

        dados_funcionario = linha.strip().split(",")
        nome_funcionario = dados_funcionario[0]
        custo = float(dados_funcionario[1])
        funcionarios_processados.append(nome_funcionario)
        custo_total += custo
        print(linha, end="")

matriz_acesso = [
    ["Livre", "Livre", "Livre"],
    ["Livre", "Livre", "Livre"],
    ["Livre", "Livre", "Livre"]
]

# DADOS DA EMPRESA

empresa = {
    "nome": "SegureTech",
    "cnpj": "12.345.678/0001-99",
    "cidade": "São Paulo",
    "ramo": "Segurança Digital"
}

print("\n====== PAINEL ======")
print("Nome da empresa:", empresa["nome"])
print("Quantidade de funcionarios processados:", len(funcionarios_processados))
print("Estado da matriz de acesso:")
for linha_matriz in matriz_acesso:
    print("  ".join(linha_matriz))
print(f"Soma total dos custos: {custo_total:.3f}")

# FUNCIONÁRIOS

funcionarios = {
    "admin": {
        "senha": "1234",
        "cargo": "Administrador"
    }
}

# RECURSOS DA EMPRESA

recursos = [
    "Sala de Servidores",
    "Escritorio Principal",
    "Laboratorio",
    "Sala de Reunioes"
]

def mostrar_empresa():

    print("\nDADOS DA EMPRESA")
    print("Nome:", empresa["nome"])
    print("CNPJ:", empresa["cnpj"])
    print("Cidade:", empresa["cidade"])
    print("Ramo:", empresa["ramo"])

def listar_recursos():

    print("\nRECURSOS DISPONIVEIS")

    for recurso in recursos:
        print("-", recurso)
        # ALUNO 2 - MATRIZ 2D DE ESTADO
# Estados dos setores: Ativo ou Inativo
setores = [
    ["Ativo", "Ativo"],
    ["Ativo", "Inativo"]
]

# Nome de cada setor da empresa
nomes = [
    ["Sala de Servidores", "Escritório Principal"],
    ["Laboratório", "Sala de Reuniões"]
]

# Mostra como está cada setor
def mostrar_setores():
    print("\n--- ESTADO DOS SETORES ---")

    for linha in range(2):
        for coluna in range(2):
            nome = nomes[linha][coluna]
            estado = setores[linha][coluna]
            print(nome, "-", estado)


# Permite mudar o estado de um setor
def alterar_estado():
    print("\nQual setor você deseja alterar?")
    print("1 - Sala de Servidores")
    print("2 - Escritório Principal")
    print("3 - Laboratório")
    print("4 - Sala de Reuniões")

    opcao = input("Digite o número do setor: ")

    if opcao == "1":
        linha, coluna = 0, 0
    elif opcao == "2":
        linha, coluna = 0, 1
    elif opcao == "3":
        linha, coluna = 1, 0
    elif opcao == "4":
        linha, coluna = 1, 1
    else:
        print("Opção inválida. Tente novamente.")
        return

    # Troca o estado atual pelo contrário
    if setores[linha][coluna] == "Ativo":
        setores[linha][coluna] = "Inativo"
    else:
        setores[linha][coluna] = "Ativo"

    print("Estado do setor atualizado!")


# Exibe os setores antes e depois da alteração
mostrar_setores()
alterar_estado()
mostrar_setores()

def cadastrar_funcionario():

    nome = input("Nome do funcionario: ")

    if nome == "":
        print("Nome invalido!")
        return

    senha = input("Senha: ")

    if senha == "":
        print("Senha invalida!")
        return

    cargo = input("Cargo: ")

    if cargo == "":
        print("Cargo invalido!")
        return

    funcionarios[nome] = {
        "senha": senha,
        "cargo": cargo
    }

    print("Funcionario cadastrado com sucesso!")

def listar_funcionarios():

    print("\nFUNCIONARIOS CADASTRADOS")

    for nome in funcionarios:

        print("Nome:", nome)
        print("Cargo:", funcionarios[nome]["cargo"])
        print("-" * 20)

def realizar_login():

    usuario = input("Usuario: ")
    senha = input("Senha: ")

    if usuario in funcionarios:

        if funcionarios[usuario]["senha"] == senha:
            print("Acesso permitido!")
            print("Cargo:", funcionarios[usuario]["cargo"])

        else:
            print("Senha incorreta!")

    else:
        print("Usuario nao encontrado!")

# MENU PRINCIPAL

while True:

    print("\n====== CONTROLE DE ACESSO ======")
    print("1 - Cadastrar funcionario")
    print("2 - Listar funcionarios")
    print("3 - Visualizar portas")
    print("4 - Ocupar porta")
    print("5 - Liberar porta")
    print("6 - Realizar login")
    print("7 - Listar recursos")
    print("8 - Dados da empresa")
    print("9 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        cadastrar_funcionario()

    elif opcao == "2":
        listar_funcionarios()

    elif opcao == "3":
        def visualizar_portas():
            ...

        visualizar_portas()

    elif opcao == "4":
        def ocupar_porta():
            ...

        ocupar_porta()

    elif opcao == "5":
        def liberar_porta():
            ...

        liberar_porta()

    elif opcao == "6":
        realizar_login()

    elif opcao == "7":
        listar_recursos()

    elif opcao == "8":
        mostrar_empresa()

    elif opcao == "9":
        print("Sistema encerrado.")
        break

    else:
        print("Opcao invalida!")

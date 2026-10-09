# DADOS DA EMPRESA

empresa = {
    "nome": "SecureTech",
    "cnpj": "12.345.678/0001-99",
    "cidade": "São Paulo",
    "ramo": "Segurança Digital"
}

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
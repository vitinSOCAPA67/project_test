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
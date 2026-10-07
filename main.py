#Cadastro e Entidades Basícas --
empresa_info = {
    "nome": "Doorlog", 
    "setor": "Segurança: Controle de Acesso",
    "cnpj": "12.345.678/0001-99",
}

recursos_ativos = [
    {"id_recurso": "CAT-01", "nome": "Catraca Principal - Recepção", "status": "Ativo"},
    {"id_recurso": "CAT-02", "nome": "Catraca Setor 1 - Servidores", "status": "Ativo"},
    {"id_recurso": "CAT-03", "nome": "Catraca Setor 2 - Estoque", "status": "Ativo"},
    {"id_recurso": "PORTA-03", "nome": "Acesso Restrito - Diretoria", "status": "Ativo"}
    
]

def exibir_empresa():
    print("===EXIBIR PERFIL DA EMPRESA===")
    
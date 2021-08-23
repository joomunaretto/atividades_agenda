class Contato:
    def __init__(self):
        self.nome = ''
        self.telefone = ''

    def Cadastrar(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def Listar(self):
        return 'Nome do contato: ' + self.nome + ', Telefone: ' + self.telefone

    def Excluir(self):
        self.nome = ''
        self.telefone = ''

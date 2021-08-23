class Tarefa:
    def __init__(self):
        self.descricao = ''
        self.status = ''

    def Criar(self, descricao, status):
        self.descricao = descricao
        self.status = status

    def Listar(self):
        return 'A tarefa ' + self.descricao + ', está com o status: ' + self.status

    def Excluir(self):
        self.descricao = ''
        self.status = ''

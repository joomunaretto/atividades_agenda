from Classes.agenda import Agenda
from Classes.tarefa import Tarefa
from Classes.contato import Contato

agenda = Agenda()
tarefa = Tarefa()
contato = Contato()

agenda.nome = input('Favor informe o nome da agenda: ')
agenda.ano = int(input('Favor informe o ano da agenda: '))

continuar = True

while continuar:
    fazer = int(input('----------------------------\nDigite 1 se quiser criar um contato \n2 se quiser listar os contatos\n3 se quiser excluir contato\n4 se quiser criar tarefa\n5 se quiser listar as tarefas\n6 se quiser excluir as tarefas: '))

    if fazer == 1:
        contato.Cadastrar('Joelma', '9 9999-9999')
        print('Contato criado com sucesso')
    elif fazer == 2:
        print(contato.Listar())
    elif fazer == 3:
        contato.Excluir()
        print('Contato excluído com sucesso')
    elif fazer == 4:
        tarefa.Criar("Ligar para o Lucas", "Pendente")
        print('Tarefa criada')
    elif fazer == 5:
        print(tarefa.Listar())
    elif fazer == 6:
        tarefa.Excluir()
        print('Tarefa excluída')
    else:
        print('Favor informar um numero de 1 a 6')
    verifica = int(input('informe 0 se quiser fazer mais um processo: '))

    if verifica == 0:
        continue
    else:
        continuar = False

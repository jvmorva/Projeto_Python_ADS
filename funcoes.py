def mostrar_menu_principal(): #Função para mostrar o menu principal.
    print("""
    Bem vindo ao sistema para gestão de dados acadêmicos.

    MENU PRINCIPAL

    1. Estudantes
    2. Disciplinas
    3. Professores
    4. Turmas
    5. Matrículas
    6. Sair
             """)
    return input("Selecione a opção desejada: ")


def mostrar_menu_operacoes(): #Função para mostrar o menu de operações.
    print("""
1. Incluir
2. Listar
3. Atualizar
4. Excluir
5. Voltar ao menu principal
            """)
    return input("Selecione a opção desejada: ")


def incluir_estudante(lista): #Função para incluir estudante
    while True:
        cod = (input("\nDigite o código do estudante: "))  # Não estou deixando o input como "int" para evitar erros ao EXCLUIR/ATUALIZAR caso outra tecla, que não seja um número int, seja clicada.
        nomeestudante = input("Digite o nome do estudante: ")
        cpfdoaluno = input("Digite o CPF do estudante: ")
        aluno = {}
        aluno["código"] = cod
        aluno["nome"] = nomeestudante
        aluno["cpf"] = cpfdoaluno
        lista.append(aluno)
        sair = input("Tecle 0 para sair e qualquer outra tecla para incluir outro estudante: ")
        if sair == "0":
            break


def listar(lista): #Função para listar. É genérica.
    for elemento in lista:
        print(elemento)
    if lista == []:
        print("Não há estudantes cadastrados")


def atualizar_estudante(lista): #Função para atualizar estudantes.
    while True:  # Loop opcional. Voltar para o menu depois de uma atualização também é ok.
        codigo_para_atualizar = input("\nDigite o código do estudante que deseja atualizar: ")  # Não estou deixando o input como "int" para evitar erros ao EXCLUIR/ATUALIZAR caso outra tecla, que não seja um número int, seja clicada.
        atualizar = None
        for aluno in lista:
            if aluno["código"] == codigo_para_atualizar:
                atualizar = aluno
                break

        if atualizar is None:
            print("\nEste código não pertence a nenhum aluno.")
        else:
            atualizar["código"] = input("Digite o novo código do estudante: ")  # Não estou deixando o input como "int" para evitar erros ao EXCLUIR/ATUALIZAR caso outra tecla, que não seja um número int, seja clicada.
            atualizar["nome"] = input("Digite o novo nome do estudante: ")
            atualizar["cpf"] = input("Digite o novo CPF do estudante: ")
            print("\nEstudante atualizado com sucesso.")
        sair = input("Tecle 0 para sair e qualquer outra tecla para incluir outro estudante: ")
        if sair == "0":
            break


def excluir(lista, chave_qualquer): #Função para excluir. É genérica.
    while True:  # Loop opcional. Voltar para o menu depois de uma exclusão também é ok.
        codigo_para_excluir = input(f"\nDigite o valor de {chave_qualquer} que deseja remover: ") #Deixamos que o usuário escolha a partir de qual chave ele vai deletar o item desejado.
        excluir = None                                                                            #Isso permite que a função se torne genérica.
        for elemento in lista:
            if elemento[chave_qualquer] == codigo_para_excluir:
                excluir = elemento
                break

        if excluir is None:
            print("\nEste código não pertence a nenhum aluno.")
        else:
            lista.remove(excluir)
            print("\nEstudante excluído com sucesso.")
        sair = input("Tecle 0 para sair e qualquer outra tecla para excluir outro estudante:")
        if sair == "0":
            break
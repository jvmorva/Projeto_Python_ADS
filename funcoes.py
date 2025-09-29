import json


def json_dump(lista, nome_arquivo):
    with open(nome_arquivo, 'w', encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False)


def json_load(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding="utf-8") as arquivo:
            lista = json.load(arquivo)
        return lista
    except:
        return []


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


def incluir_estudante(nome_arquivo): #Função para incluir estudante
    while True:
        estudantes = json_load(nome_arquivo)
        cod = (input("\nDigite o código do estudante: "))  # Não estou deixando o input como "int" para evitar erros ao EXCLUIR/ATUALIZAR caso outra tecla, que não seja um número int, seja clicada.
        nomeestudante = input("Digite o nome do estudante: ")
        cpfdoaluno = input("Digite o CPF do estudante: ")
        aluno = {}
        aluno["código"] = cod
        aluno["nome"] = nomeestudante
        aluno["cpf"] = cpfdoaluno
        estudantes.append(aluno)
        json_dump(estudantes, nome_arquivo)
        sair = input("Tecle 0 para sair e qualquer outra tecla para incluir outro estudante: ")
        if sair == "0":
            break


def listar(nome_arquivo): #Função para listar. É genérica.
    estudantes = json_load(nome_arquivo) #Carrega a lista atual.
    for elemento in estudantes:
        print(elemento)
    if estudantes == []:
        print("Não há estudantes cadastrados")


def atualizar_estudante(nome_arquivo): #Função para atualizar estudantes.
    while True:  # Loop opcional. Voltar para o menu depois de uma atualização também é ok.
        estudantes = json_load(nome_arquivo) #Carrega a lista atual.

        codigo_para_atualizar = input("\nDigite o código do estudante que deseja atualizar: ")  # Não estou deixando o input como "int" para evitar erros ao EXCLUIR/ATUALIZAR caso outra tecla, que não seja um número int, seja clicada.
        atualizar = None
        for aluno in estudantes:
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

        json_dump(estudantes, nome_arquivo) #Da "dump" nas novas informações.
        sair = input("Tecle 0 para sair e qualquer outra tecla para incluir outro estudante: ")
        if sair == "0":
            break


def excluir(nome_arquivo, chave_qualquer): #Função para excluir. É genérica.
    while True:  # Loop opcional. Voltar para o menu depois de uma exclusão também é ok.
        estudantes = json_load(nome_arquivo)
        codigo_para_excluir = input(f"\nDigite o valor de {chave_qualquer} que deseja remover: ") #Deixamos que o usuário escolha a partir de qual chave ele vai deletar o item desejado.
        excluir = None                                                                            #Isso permite que a função se torne genérica.
        for elemento in estudantes:
            if elemento[chave_qualquer] == codigo_para_excluir:
                excluir = elemento
                break

        if excluir is None:
            print("\nEste código não pertence a nenhum aluno.")
        else:
            estudantes.remove(excluir)
            print("\nEstudante excluído com sucesso.")
        json_dump(estudantes, nome_arquivo)
        sair = input("Tecle 0 para sair e qualquer outra tecla para excluir outro estudante:")
        if sair == "0":
            break
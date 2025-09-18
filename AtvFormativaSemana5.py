#Aluno: João Vitor Morva Yunes
#Curso: Análise e Desenvolvimento de Sistemas

listaestudantes = []

while True: #loop principal
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
    menuprincipal = input("Selecione a opção desejada: ")
    if menuprincipal == "6": #Encerra o programa.
        print("\nVocê saiu do programa, até logo.")
        break

    while True: #loop secundário
        if menuprincipal == "1":
            print("""
Estudantes - MENU DE OPERAÇÕES

1. Incluir
2. Listar
3. Atualizar
4. Excluir
5. Voltar ao menu principal
            """)
            menudeopp = input("Selecione a opção desejada: ") # "menudeopp" significa menu de operações.

            if menudeopp == "1": #Incluir estudantes
                while True:
                    print("\nIncluir estudante")
                    cod = (input("Digite o código do estudante: ")) #Não estou deixando o input como "int" para evitar erros ao EXCLUIR/ATUALIZAR caso outra tecla, que não seja um número int, seja clicada.
                    nomeestudante = input("Digite o nome do estudante: ")
                    cpfdoaluno = input("Digite o CPF do estudante: ")
                    aluno = {}
                    aluno["código"] = cod
                    aluno["nome"] = nomeestudante
                    aluno["cpf"] = cpfdoaluno
                    listaestudantes.append(aluno)
                    sair = input("Tecle 0 para sair e qualquer outra tecla para incluir outro estudante: ")
                    if sair == "0":
                        break
            elif menudeopp == "2": #Listar estudantes
                print("\nLista de estudantes:\n")
                for estudante in listaestudantes:
                    print(estudante)
                if listaestudantes == []:
                    print("Não há estudantes cadastrados")
            elif menudeopp == "3":
                while True:  # Loop opcional. Voltar para o menu depois de uma atualização também é ok.
                    print("\nAtualizar estudante")
                    codigo_para_atualizar = input("Digite o código do estudante que deseja atualizar: ") #Não estou deixando o input como "int" para evitar erros ao EXCLUIR/ATUALIZAR caso outra tecla, que não seja um número int, seja clicada.
                    atualizar = None
                    for aluno in listaestudantes:
                        if aluno["código"] == codigo_para_atualizar:
                            atualizar = aluno
                            break

                    if atualizar is None:
                        print("\nEste código não pertence a nenhum aluno.")
                    else:
                        atualizar["código"] = input("Digite o novo código do estudante: ") #Não estou deixando o input como "int" para evitar erros ao EXCLUIR/ATUALIZAR caso outra tecla, que não seja um número int, seja clicada.
                        atualizar["nome"] = input("Digite o novo nome do estudante: ")
                        atualizar["cpf"] = input("Digite o novo CPF do estudante: ")
                        print("\nEstudante atualizado com sucesso.")
                    sair = input("Tecle 0 para sair e qualquer outra tecla para atualizar outro estudante:")
                    if sair == "0":
                        break
            elif menudeopp == "4":
                while True: # Loop opcional. Voltar para o menu depois de uma exclusão também é ok.
                    print("\nExcluir estudante")
                    codigo_para_excluir = input("Digite o código do estudante que deseja remover: ") #Não estou deixando o input como "int" para evitar erros ao EXCLUIR/ATUALIZAR caso outra tecla, que não seja um número int, seja clicada.
                    excluir = None
                    for aluno in listaestudantes:
                        if aluno["código"] == codigo_para_excluir:
                            excluir = aluno
                            break

                    if excluir is None:
                        print("\nEste código não pertence a nenhum aluno.")
                    else:
                        listaestudantes.remove(excluir)
                        print("\nEstudante excluído com sucesso.")
                    sair = input("Tecle 0 para sair e qualquer outra tecla para excluir outro estudante:")
                    if sair == "0":
                        break
            elif menudeopp == "5":
                break
            else:
                print("\nComando inválido, selecione uma das opções abaixo")

# Abaixo são os tópicos ainda em desenvolvimento.
        elif menuprincipal == "2":
            print("\nDisciplinas - EM DESENVOLVIMENTO - Retornando ao menu principal")
            break
        elif menuprincipal == "3":
            print("\nProfessores - EM DESENVOLVIMENTO - Retornando ao menu principal")
            break
        elif menuprincipal == "4":
            print("\nTurmas - EM DESENVOLVIMENTO - Retornando ao menu principal")
            break
        elif menuprincipal == "5":
            print("\nMatrículas - EM DESENVOLVIMENTO - Retornando ao menu principal")
            break
        else:
            print("\nComando inválido - Retornando ao menu principal")
            break
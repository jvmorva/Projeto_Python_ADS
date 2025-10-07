from funcoes import *

#Aluno: João Vitor Morva Yunes
#Curso: Análise e Desenvolvimento de Sistemas

arquivo_estudantes = "estudantes.json"
arquivo_disciplinas = "disciplinas.json"
arquivo_professores = "professores.json"
arquivo_turmas = "turmas.json"
arquivo_matriculas = "matriculas.json"

while True: #loop principal
    menuprincipal = mostrar_menu_principal()
    if menuprincipal == "6": #Encerra o programa.
        print("\nVocê saiu do programa, até logo.")
        break

    while True: #loop secundário
        if menuprincipal == "1":
            print("\nEstudantes - MENU DE OPERAÇÕES")
            menudeopp = mostrar_menu_operacoes() #menudeopp significa menu de operações.

            if menudeopp == "1": #Incluir estudantes
                print("\nIncluir estudante")
                incluir(arquivo_estudantes, "código", "nome", "CPF")
            elif menudeopp == "2": #Listar estudantes
                print("\nLista de estudantes:\n")
                listar(arquivo_estudantes)
            elif menudeopp == "3":
                print("\nAtualizar estudante")
                atualizar(arquivo_estudantes, "código", "nome", "CPF")
            elif menudeopp == "4":
                print("\nExcluir estudante")
                excluir(arquivo_estudantes,"código")
            elif menudeopp == "5":
                break
            else:
                print("\nComando inválido, selecione uma das opções abaixo")

        elif menuprincipal == "2":
            print("\nDisciplinas - MENU DE OPERAÇÕES")
            menudeopp = mostrar_menu_operacoes() #menudeopp significa menu de operações.

            if menudeopp == "1":
                print("\nIncluir disciplina")
                incluir(arquivo_disciplinas, "código", "nome")
            elif menudeopp == "2":
                print("\nLista de disciplinas:\n")
                listar(arquivo_disciplinas)
            elif menudeopp == "3":
                print("\nAtualizar disciplina")
                atualizar(arquivo_disciplinas, "código", "nome")
            elif menudeopp == "4":
                print("\nExcluir disciplina")
                excluir(arquivo_disciplinas,"código")
            elif menudeopp == "5":
                break
            else:
                print("\nComando inválido, selecione uma das opções abaixo")

        elif menuprincipal == "3":
            print("\nProfessores - MENU DE OPERAÇÕES")
            menudeopp = mostrar_menu_operacoes()  # menudeopp significa menu de operações.

            if menudeopp == "1":
                print("\nIncluir professor")
                incluir(arquivo_professores, "código", "nome", "CPF")
            elif menudeopp == "2":
                print("\nLista de professores:\n")
                listar(arquivo_professores)
            elif menudeopp == "3":
                print("\nAtualizar professor")
                atualizar(arquivo_professores, "código", "nome", "CPF")
            elif menudeopp == "4":
                print("\nExcluir professor")
                excluir(arquivo_disciplinas, "código")
            elif menudeopp == "5":
                break
            else:
                print("\nComando inválido, selecione uma das opções abaixo")

        elif menuprincipal == "4":
            print("\nTurmas - MENU DE OPERAÇÕES")
            menudeopp = mostrar_menu_operacoes()  # menudeopp significa menu de operações.

            if menudeopp == "1":
                print("\nIncluir turma")
                incluir(arquivo_turmas, "código da turma", "código do professor", "código da disciplina")
            elif menudeopp == "2":
                print("\nLista de turmas:\n")
                listar(arquivo_turmas)
            elif menudeopp == "3":
                print("\nAtualizar turma")
                atualizar(arquivo_turmas, "código da turma", "código do professor", "código da disciplina")
            elif menudeopp == "4":
                print("\nExcluir turma")
                excluir(arquivo_turmas, "código da turma")
            elif menudeopp == "5":
                break
            else:
                print("\nComando inválido, selecione uma das opções abaixo")

        elif menuprincipal == "5":
            print("\nMatrículas - MENU DE OPERAÇÕES")
            menudeopp = mostrar_menu_operacoes()  # menudeopp significa menu de operações.

            if menudeopp == "1":
                print("\nIncluir matrícula")
                incluir(arquivo_matriculas, "código da turma", "código do estudante")
            elif menudeopp == "2":
                print("\nLista de matrículas:\n")
                listar(arquivo_matriculas)
            elif menudeopp == "3":
                print("\nAtualizar matrícula")
                atualizar(arquivo_matriculas, "código da turma", "código do estudante")
            elif menudeopp == "4":
                print("\nExcluir matrícula")
                excluir(arquivo_matriculas, "código da turma")
            elif menudeopp == "5":
                break
            else:
                print("\nComando inválido, selecione uma das opções abaixo")

        else:
            print("\nComando inválido - Retornando ao menu principal")
            break



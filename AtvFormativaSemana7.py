from funcoes import *

#Aluno: João Vitor Morva Yunes
#Curso: Análise e Desenvolvimento de Sistemas

arquivo_json = "estudantes.json"

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
                incluir_estudante(arquivo_json)
            elif menudeopp == "2": #Listar estudantes
                print("\nLista de estudantes:\n")
                listar(arquivo_json)
            elif menudeopp == "3":
                print("\nAtualizar estudante")
                atualizar_estudante(arquivo_json)
            elif menudeopp == "4":
                print("\nExcluir estudante")
                excluir(arquivo_json,"código")
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



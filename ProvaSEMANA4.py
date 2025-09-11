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
                    nomeestudante = (input("Digite o nome do estudante: "))
                    listaestudantes.append(nomeestudante)
                    print("Estudante incluído com sucesso.")
                    sair = input("Tecle 0 para sair e qualquer outra tecla para incluir outro estudante:")
                    if sair == "0":
                        break
            elif menudeopp == "2": #Listar estudantes
                print("\nLista de estudantes:\n")
                for estudante in listaestudantes:
                    print(estudante)
                if listaestudantes == []:
                    print("Não há estudantes cadastrados")
            elif menudeopp == "3":
                print("\nAtualizar - ESTA FUNÇÃO AINDA NÃO ESTÁ DISPONÍVEL")
            elif menudeopp == "4":
                print("\nExcluir - ESTA FUNÇÃO AINDA NÃO ESTÁ DISPONÍVEL")
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


while (True):
    print("""
    "Bem vindo ao sistema para gestão de dados acadêmicos."

    MENU PRINCIPAL

    1. Estudantes
    2. Disciplinas
    3. Professores
    4. Turmas
    5. Matrículas
         """)
    menuprincipal = int(input("Selecione a opção desejada: "))

    # Condicional do menu principal:

    if menuprincipal == 1:
        print("""
    Estudantes - MENU DE OPERAÇÕES

    1. Incluir
    2. Listar
    3. Atualizar
    4. Excluir
    5. Voltar ao menu principal
        """)
        menudeopp = int(input("Selecione a opção desejada: "))
    elif menuprincipal == 2:
        print("""
    Disciplinas - MENU DE OPERAÇÕES

    1. Incluir
    2. Listar
    3. Atualizar
    4. Excluir
    5. Voltar ao menu principal
        """)
        menudeopp = int(input("Selecione a opção desejada: "))
    elif menuprincipal == 3:
        print("""
    Professores - MENU DE OPERAÇÕES

    1. Incluir
    2. Listar
    3. Atualizar
    4. Excluir
    5. Voltar ao menu principal
        """)
        menudeopp = int(input("Selecione a opção desejada: "))
    elif menuprincipal == 4:
        print("""
    Turmas - MENU DE OPERAÇÕES

    1. Incluir
    2. Listar
    3. Atualizar
    4. Excluir
    5. Voltar ao menu principal
        """)
        menudeopp = int(input("Selecione a opção desejada: "))
    elif menuprincipal == 5:
        print("""
    Matrículas - MENU DE OPERAÇÕES

    1. Incluir
    2. Listar
    3. Atualizar
    4. Excluir
    5. Voltar ao menu principal
        """)
        menudeopp = int(input("Selecione a opção desejada: "))
    else:
        print("Comando inválido")

    # Condicional do menu de operações:

    while (True):
        if menudeopp == 1:
            print("""
    Incluir

    Esta função ainda não está disponível.

    Matrículas - MENU DE OPERAÇÕES
    1. Incluir
    2. Listar
    3. Atualizar
    4. Excluir
    5. Voltar ao menu principal
               """
                  )
        elif menudeopp == 2:
            print("""
    Listar

    Esta função ainda não está disponível.

    Matrículas - MENU DE OPERAÇÕES
    1. Incluir
    2. Listar
    3. Atualizar
    4. Excluir
    5. Voltar ao menu principal
                """)
        elif menudeopp == 3:
            print("""
    Atualizar

    Esta função ainda não está disponível.

    Matrículas - MENU DE OPERAÇÕES
    1. Incluir
    2. Listar
    3. Atualizar
    4. Excluir
    5. Voltar ao menu principal
                """)
        elif menudeopp == 4:
            print("""
    Excluir

    Esta função ainda não está disponível.

    Matrículas - MENU DE OPERAÇÕES
    1. Incluir
    2. Listar
    3. Atualizar
    4. Excluir
    5. Voltar ao menu principal
                """)
        elif menudeopp == 5:
            break
        else:
            print("Comando inválido, selecione uma das opções acima")

        menudeopp = int(input("Selecione a opção desejada: "))



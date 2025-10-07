import json


def json_dump(lista, nome_arquivo): #Função para ADICIONAR informações no arquivo json.
    with open(nome_arquivo, 'w', encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False)


def json_load(nome_arquivo): #Função para MOSTRAR informações no arquivo json.
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


def incluir(nome_arquivo, chave1, chave2="vazio", chave3="vazio"): #Função para incluir. É genérica.
    while True:
        lista = json_load(nome_arquivo)
        dicionario = {}
        for chave in [chave1, chave2, chave3]:
            if chave != "vazio": #Só pede "input" para os parâmetros passados, ignorando os de valor padrão.
                while True:
                    valor_da_chave = input(f"Digite o valor de {chave}: ")
                    if valor_da_chave == "": #Impede que o usuário possa deixar o campo vazio.
                        print("Este campo não pode estar vazio")
                        continue
                    if valor_da_chave.isdigit(): #Converte o valor para "int" caso o valor digitado seja um número inteiro. Infelizmente não existe uma função como esta para converter para float.
                        valor_da_chave = int(valor_da_chave)
                    dicionario[chave] = valor_da_chave
                    break

        lista.append(dicionario)
        json_dump(lista, nome_arquivo)
        print("\nInclusão bem sucedida.")
        sair = input("Tecle 0 para sair e qualquer outra tecla para realizar uma nova inclusão: ")
        if sair == "0":
            break


def listar(nome_arquivo): #Função para listar. É genérica.
    lista = json_load(nome_arquivo)
    for elemento in lista:
        print(elemento)
    if lista == []:
        print("Não há dados cadastrados")


def atualizar(nome_arquivo, chave1, chave2="vazio", chave3="vazio"): #Função para atualizar. É genérica.
    while True:  #Loop opcional. Voltar para o menu depois de uma atualização também é ok.
        lista = json_load(nome_arquivo)

        codigo_para_atualizar = input(f"\nDigite o valor do {chave1} do elemento que deseja atualizar: ")
        if codigo_para_atualizar.isdigit(): #Converte o valor para "int" caso o valor digitado seja um número inteiro.
           codigo_para_atualizar = int(codigo_para_atualizar)

        atualizar = None
        for elemento in lista:
            if elemento[chave1] == codigo_para_atualizar:
                atualizar = elemento
                break

        if atualizar is None:
            print("\nEste código não pertence a nenhum aluno.")
        else:
            for chave in [chave1, chave2, chave3]:
                if chave != "vazio": #Só pede "input" para os parâmetros passados, ignorando os de valor padrão.
                    while True:
                        novo_valor = input(f"Digite o novo valor de {chave}: ")
                        if novo_valor == "": #Impede que o usuário possa deixar o campo vazio.
                            print("Este campo não pode estar vazio")
                            continue
                        if novo_valor.isdigit(): #Converte o valor para "int" caso o valor digitado seja um número inteiro.
                            novo_valor = int(novo_valor)
                        atualizar[chave] = novo_valor
                        break

        json_dump(lista, nome_arquivo)
        print("\nAtualização bem sucedida.")
        sair = input("Tecle 0 para sair e qualquer outra tecla para incluir outro estudante: ")
        if sair == "0":
            break


def excluir(nome_arquivo, chave_qualquer): #Função para excluir. É genérica.
    while True:  #Loop opcional. Voltar para o menu depois de uma exclusão também é ok.
        lista = json_load(nome_arquivo)
        codigo_para_excluir = input(f"\nDigite o valor de {chave_qualquer} do item que deseja remover: ") #Deixamos que o usuário escolha a partir de qual chave ele vai deletar o item desejado.
        if codigo_para_excluir.isdigit(): #Converte o valor para "int" caso o valor digitado seja um número inteiro.
            codigo_para_excluir = int(codigo_para_excluir)

        excluir = None
        for elemento in lista:
            if elemento[chave_qualquer] == codigo_para_excluir:
                excluir = elemento
                break

        if excluir is None:
            print("\nEste código não pertence a nenhum item.")
        else:
            lista.remove(excluir)
            print("\nItem excluído com sucesso.")

        json_dump(lista, nome_arquivo)
        sair = input("Tecle 0 para sair e qualquer outra tecla para excluir outro item:")
        if sair == "0":
            break
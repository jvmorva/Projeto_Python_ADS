import json

# UTILIDADES (JSON) --------------------------------------------------------

def json_dump(lista, nome_arquivo): #Função para ADICIONAR (gravar) informações no arquivo json.
    with open(nome_arquivo, 'w', encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False)


def json_load(nome_arquivo): #Função para MOSTRAR (carregar) informações no arquivo json.
    try:
        with open(nome_arquivo, 'r', encoding="utf-8") as arquivo:
            lista = json.load(arquivo)
        return lista
    except:
        return []


# FUNÇÕES AUXILIARES --------------------------------------------------------

def novo_valor(mensagem):
    while True:
        valor = input(mensagem)

        if valor == "":
            print("Este campo não pode estar vazio")
            continue

        return valor


def buscar_elemento(lista, chave, valor):
    for elemento in lista:
        if elemento[chave] == valor:
            return elemento
    return None


# CRUD --------------------------------------------------------

def incluir(nome_arquivo, chave1, chave2="vazio", chave3="vazio"): #Função para incluir. É genérica.
    while True:
        lista = json_load(nome_arquivo)
        dicionario = {}
        for chave in [chave1, chave2, chave3]:
            if chave != "vazio": #Só pede "input" para os parâmetros passados, ignorando os de valor padrão.
                dicionario[chave] = novo_valor(f"Digite o valor de {chave}: ") #uso da função "novo_valor"

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

        elemento = buscar_elemento(lista, chave1, codigo_para_atualizar) #uso da função "buscar_elemento"

        if elemento is None:
            print("\nEste código não pertence a nenhum item.")
        else:
            for chave in [chave1, chave2, chave3]:
                if chave != "vazio": #Só pede "input" para os parâmetros passados, ignorando os de valor padrão.
                    elemento[chave] = novo_valor(f"Digite o novo valor de {chave}: ") #uso da função "novo_valor"

            json_dump(lista, nome_arquivo)
            print("\nAtualização bem sucedida.")

        sair = input("Tecle 0 para sair e qualquer outra tecla para atualizar outro item: ")
        if sair == "0":
            break


def excluir(nome_arquivo, chave_qualquer): #Função para excluir. É genérica.
    while True:  #Loop opcional. Voltar para o menu depois de uma exclusão também é ok.
        lista = json_load(nome_arquivo)
        codigo_para_excluir = input(f"\nDigite o valor de {chave_qualquer} do item que deseja remover: ") #Deixamos que o usuário escolha a partir de qual chave ele vai deletar o item desejado.

        elemento = buscar_elemento(lista, chave_qualquer, codigo_para_excluir) #uso da função "buscar_elemento"

        if elemento is None:
            print("\nEste código não pertence a nenhum item.")
        else:
            lista.remove(elemento)
            print("\nItem excluído com sucesso.")

        json_dump(lista, nome_arquivo)
        sair = input("Tecle 0 para sair e qualquer outra tecla para excluir outro item:")
        if sair == "0":
            break


# MENUS --------------------------------------------------------

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
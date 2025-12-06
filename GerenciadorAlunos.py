"""
GERENCIADOR DE ALUNOS - SISTEMA DE CADASTRO ESCOLAR (CONSOLE)

PROJETO: Sistema CRUD básico para cadastro e gerenciamento de alunos
NIVEL: Iniciante/Intermediário (similar ao Gerenciador de Agenda)
OBJETIVO: Praticar listas, dicionários, loops, condicionais e funções

FUNCIONALIDADES PLANEJADAS:
├── 1. CADASTRAR_ALUNO() → Adiciona novo aluno na lista com validação de ID único
├── 2. LISTAR_ALUNOS() → Mostra todos os alunos formatados em tabela simples
├── 3. BUSCAR_ALUNO() → Procura por ID ou nome 
├── 4. ATUALIZAR_ALUNO() → Edita campos específicos de um aluno pelo ID
├── 5. REMOVER_ALUNO() → Apaga aluno pelo ID com confirmação
└── 6. SAIR → Sair do Sistema

ESTRUTURA DE DADOS:
- lista_alunos = []  # Lista de dicionários
- Cada aluno: {'id': str, 'nome': str, 'idade': int, 'curso': str, 'media': float}

AUTOR: Janerson Alves | DATA: 03/12/2025

"""

import os

#Função de cadastrar alunos, que recebe como argumento a lista de alunos, nome, idade, curso e média do aluno
def cadastrar_aluno(alunos, nome, idade, curso, media):
    #Auto Incrementar o ID
    novo_id = str(len(alunos) + 1)
    #Armazena na variavel se o aluno está aprovado ou reprovado!
    status = "Aprovado" if media >= 6 else "Reprovado"
    #Cria o dicionario com os dados do aluno
    novo_aluno = {
        "id": novo_id,
        "nome" : nome,
        "idade" : idade,
        "curso" : curso,
        "media" : media,
        "status": status
    }
    #Adiciona as Informações do dicionario do aluno para a lista de alunos
    alunos.append(novo_aluno)
    #Mostra na tela que o Aluno foi adicionado com sucesso.
    print(f"Aluno {nome} Adicionado com sucesso!")
    print(type(novo_id))
    return

#Função que lista a lista de alunos
def listar_alunos():
    print("#" * 30, "Lista de Alunos", "#" * 30)
    #Itera sobre cada valor da lista usando enumerate para pegar o indice da lista e o valor do aluno.
    for indice, aluno in enumerate(lista_alunos):
        #Coleta o valor do indice do dicionario
        id_aluno = aluno["id"]
        nome_aluno = aluno["nome"]
        idade_aluno = aluno["idade"]
        curso_aluno = aluno["curso"]
        media_aluno = aluno["media"]
        status_aluno = aluno["status"]
        #mostra na tela as informações do aluno de uma forma personalizada
        print(f"Id: {id_aluno} | Nome: {nome_aluno} | Idade: {idade_aluno} | Curso: {curso_aluno} | Média: {media_aluno} | Status: {status_aluno}")
    return

def buscar_aluno_por_id_nome(alunos, nome_id):
    #Seta uma variavel com padrão false para verificar se encontrou o aluno
    encontrado = False
    #Itera sobre cada valor da lista usando enumerate para pegar o indice da lista e o valor do aluno.
    for indice, aluno in enumerate(alunos):
        id_aluno = aluno["id"]
        nome_aluno = aluno["nome"]
        idade_aluno = aluno["idade"]
        curso_aluno = aluno["curso"]
        media_aluno = aluno["media"]
        status_aluno = aluno["status"]
        #Vefica se o valor digitado pelo usuario existe ou no ID ou no NOME do aluno
        if id_aluno == nome_id or nome_aluno == nome_id:
            print("Aluno encontrado!")
            print(f"Id: {id_aluno} | Nome: {nome_aluno} | Idade: {idade_aluno} | Curso: {curso_aluno} | Média: {media_aluno} | Status: {status_aluno}")
            encontrado = True
            break
    #Executa se caso o ALUNO náo for encontrado na lista de alunos
    if not encontrado:
        limpar_tela()
        print("Aluno não cadastrado!")

def atualizar_aluno(alunos, nome_id):
    encontrado = False

    #Itera sobre cada valor da lista usando enumerate para pegar o indice da lista e o valor do aluno.
    for indice, aluno in enumerate(alunos):
        id_aluno = aluno["id"]
        nome_aluno = aluno["nome"]
        media_aluno = aluno["media"]
     
        #Vefica se o valor digitado pelo usuario existe ou no ID ou no NOME do aluno
        if id_aluno == nome_id or nome_aluno == nome_id:
            encontrado = True
            limpar_tela()
            print("Aluno encontrado!")
            listar_alunos()
            #Pede para o usuário digitar a opção desejada
            editar_aluno = input("Digite a opção para editar o aluno [1] - Idade [2] - Curso [3] - Nota: ")
            #Altera a Idade do Aluno
            if editar_aluno == "1":
                limpar_tela()
                idade_nova = int(input("Digite a nova idade do aluno: "))
                aluno["idade"] = idade_nova
                print("Alterado a idade do aluno com sucesso!")
                listar_alunos()
            #Altera o Curso do aluno
            elif editar_aluno == "2":
                limpar_tela()
                curso_novo = input("Digite o curso novo do aluno? ")
                aluno["curso"] = curso_novo
                print("Alterado o curso do aluno com sucesso!")
                listar_alunos()
            #Altera a nota do aluno e muda o status caso a nota altere EX: Se estiver APROVADO e a nota nova for menor que 6, ele muda para REPROVADO
            elif editar_aluno == "3":
                limpar_tela()
                nota_nova = float(input("Digite a nova nota do aluno: "))
                if nota_nova >= 0 and media_aluno <= 10:
                    #Armazena na variavel se o aluno está aprovado ou reprovado!
                    status = "Aprovado" if nota_nova >= 6 else "Reprovado"
                    aluno["media"] = nota_nova
                    aluno["status"] = status
                    print("Alterado a nota do aluno com sucesso!")
                    listar_alunos()
                else:
                    print("Favor digitar uma nota entre 0 e 10")

    #Executa se caso o ALUNO náo for encontrado na lista de alunos
    if not encontrado:
        limpar_tela()
        print("Aluno não cadastrado!")

def remover_aluno(alunos, id_aluno):
    encontrado = False
    for indice, aluno in enumerate(alunos):
        if aluno["id"] == id_aluno:
            encontrado = True
            confirmacao_remover = input((f"Deseja realmente Remover o Aluno {aluno["nome"]} [1] - SIM [2] - NÄO: "))
            if confirmacao_remover == "1":
                limpar_tela()
                del alunos[indice]
                print("Aluno Removido com sucesso!")
                listar_alunos()
                
            elif confirmacao_remover == "2":
                limpar_tela()
                print("Aluno não será removido!")
                listar_alunos()
                
            else:
                print("opção invalida!")

    if not encontrado:
        limpar_tela()
        print("ID do aluno inexistente, favor digitar um ID valido")



def limpar_tela():
    os.system("cls")
    return



lista_alunos = []

#Criando o Loop Do menu
while True:
    print("#"*30, "Cadastro de alunos", "#"*30)
    print("1 - Cadastrar Alunos")
    print("2 - Listar Alunos")
    print("3 - Buscar Aluno")
    print("4 - Atualizar Aluno")
    print("5 - Remover Aluno")
    print("6 - Sair")

    try:
        escolha = int(input("Digite a opção desejada: "))

        if escolha == 1:
            #Limpa a tela
            limpar_tela()
            #Mostra na tela o cabeálho
            print("#" * 30, "Cadastro de Aluno", "#" * 30)
            #Armazena as informações do aluno
            nome_aluno = input("Digite o nome do aluno: ")
            idade_aluno = int(input("Digite a idade do aluno: "))
            curso_aluno = input("Digite o Curso do aluno: ")
            media_aluno = float(input(f"Digite a média do aluno no curso {curso_aluno} de 0 a 10: "))
            #Verifica se a media do aluno e entre 0 e 10 e se a idade e entre 4 e 99
            if (media_aluno >= 0 and media_aluno <= 10) or (idade_aluno >= 4 and idade_aluno <= 99):
                #Chama a função que cadastra e grava na lista!
                cadastrar_aluno(lista_alunos, nome_aluno, idade_aluno, curso_aluno, media_aluno)
            #Caso as verificações não sejam verdadeiras
            else:
                limpar_tela()
                print("ERROR: A média do aluno tem que ser entre 0 e 10, tente novamente!")

        elif escolha == 2:
            listar_alunos()
        elif escolha == 3:
            print("#" * 30, "Buscar Aluno", "#" * 30)
            escolha_id_nome = input("Digite o ID ou NOME do aluno a ser pesquisado: ")
            limpar_tela()
            buscar_aluno_por_id_nome(lista_alunos, escolha_id_nome)
        elif escolha == 4:
            limpar_tela()
            editar_dados_aluno = input("Digite o Nome ou ID do aluno para ser editado: ")
            atualizar_aluno(lista_alunos, editar_dados_aluno)
        elif escolha == 5:
            limpar_tela()
            id_aluno = input("Digite o ID do aluno a ser excluido: ")
            remover_aluno(lista_alunos, id_aluno)
        elif escolha == 6:
            break


    except ValueError as e:
        limpar_tela()
        print("ERROR: Valor Invalido, favor digitar um valor valido!")
# Gerenciador de Alunos (Console)

Sistema de cadastro e gerenciamento de alunos em modo console, desenvolvido em Python, focado em prática de conceitos básicos de programação e CRUD em memória.

## 🎯 Objetivo

Este projeto foi criado com o objetivo de praticar:

- Listas e dicionários
- Estruturas de repetição (loops)
- Condicionais
- Funções
- Manipulação simples de dados em memória

Nível sugerido: **Iniciante / Intermediário** (similar a um gerenciador de agenda em console). [web:4]

## 🧠 Funcionalidades

O sistema é um CRUD básico de alunos, com as seguintes operações:

- `cadastrar_aluno()`  
  Adiciona um novo aluno à lista, gerando um ID automaticamente e calculando o status de aprovação com base na média.

- `listar_alunos()`  
  Lista todos os alunos cadastrados em uma saída formatada no console.

- `buscar_aluno_por_id_nome()`  
  Permite buscar um aluno pelo **ID** ou pelo **nome**.s

- `atualizar_aluno()`  
  Atualiza campos específicos (idade, curso ou nota) de um aluno, identificado por ID ou nome, recalculando o status de aprovação quando a nota é alterada.

- `remover_aluno()`  
  Remove um aluno da lista a partir do ID, com confirmação antes da exclusão.

- Opção `Sair`  
  Encerra o sistema pelo menu principal.

## 🗂 Estrutura de Dados

Os alunos são armazenados em memória em uma lista de dicionários:

lista_alunos = []

Exemplo de estrutura de um aluno  
{  
"id": str, # ID gerado automaticamente (ex: "1", "2", "3"...)  
"nome": str,  
"idade": int,  
"curso": str,  
"media": float,  
"status": str # "Aprovado" ou "Reprovado" calculado pela média  
}  


A validação básica de dados inclui verificação de faixa de média (0 a 10) e de idade (4 a 99 anos). [web:6]

## 📌 Como Funciona o Menu

Ao executar o script Python, o usuário vê um menu interativo no console:

1. Cadastrar Alunos  
2. Listar Alunos  
3. Buscar Aluno (por ID ou Nome)  
4. Atualizar Aluno (idade, curso ou nota)  
5. Remover Aluno (por ID)  
6. Sair  

Todas as interações são feitas via `input()` e as mensagens são exibidas no terminal. O projeto utiliza a função `os.system("cls")` para limpar a tela em ambiente Windows. [web:1]

## ▶️ Como Executar

1. Certifique-se de ter o **Python 3** instalado na sua máquina. [web:4]  
2. Clone este repositório:


3. Acesse a pasta do projeto:


4. Execute o script principal:


> Observação: em sistemas Linux ou macOS, adapte o comando de limpar tela (`cls` → `clear`) se desejar compatibilidade multiplataforma. [web:15]

## 🛠 Tecnologias Utilizadas

- Python 3.x
- Modo console / terminal
- Estruturas de dados básicas (lista e dicionário) [web:4]

## 👤 Autor

Projeto desenvolvido por **Janerson Alves**  
📅 Data de criação: **03/12/2025**

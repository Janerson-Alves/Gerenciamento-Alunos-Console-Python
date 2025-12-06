# 🎓 Gerenciador de Alunos - Sistema Console

Este é um projeto de desenvolvimento em Python, implementado em modo console, com foco na prática e consolidação dos princípios básicos de programação e operações de **CRUD** (*Create, Read, Update, Delete*) em memória. É um excelente exercício para quem está no nível **Iniciante/Intermediário**.

---

## 🎯 Foco e Aprendizado

O projeto foi meticulosamente desenhado para fortalecer a compreensão e aplicação prática dos seguintes pilares da programação em Python:

* **Estruturas Fundamentais:** Domínio de **Listas** e **Dicionários** como ferramentas principais para manipulação de coleções e objetos complexos.
* **Controle de Fluxo:** Implementação eficiente de **laços de repetição (loops)** para navegação e **condicionais** para validação de regras de negócio.
* **Modularidade:** Uso de **Funções** dedicadas para isolar e gerenciar cada operação (CRUD), promovendo código limpo e reutilizável.
* **Gestão de Dados em Memória:** Simulação de um sistema de cadastro onde os dados residem na memória enquanto o programa é executado.

---

## 🧠 Conjunto de Funcionalidades

O sistema opera como um gerenciador de dados de alunos, executando todas as operações CRUD de maneira intuitiva via terminal:

| Operação | Descrição |
| :--- | :--- |
| **Cadastrar** | Adiciona um aluno, gerando um **ID** sequencial e calculando o **Status de Aprovação** automaticamente com base na média inserida. |
| **Listar** | Exibe a lista completa de alunos em um formato de tabela organizado no console. |
| **Buscar** | Permite localizar um aluno rapidamente usando seu **ID** único ou o **Nome** (com busca *case-insensitive*). |
| **Atualizar** | Modifica dados como idade, curso ou nota de um aluno. O Status de Aprovação é **recalculado dinamicamente** sempre que a nota é alterada. |
| **Remover** | Exclui um cadastro da lista após a confirmação do usuário. |
| **Sair** | Encerra a aplicação pelo menu principal. |

---

## 🗂 Estrutura de Dados

Os dados dos alunos são armazenados em uma estrutura Python nativa: uma **lista de dicionários** (`lista_alunos = []`).

Cada aluno é representado por um dicionário com as seguintes chaves:

json  
{  
"id": "1",          // String sequencial gerada pelo sistema  
"nome": "Nome do Aluno",  
"idade": 25,        // Validação: 4 a 99 anos  
"curso": "Engenharia",  
"media": 8.5,       // Validação: 0.0 a 10.0  
"status": "Aprovado"// Calculado: "Aprovado" (media >= 6) ou "Reprovado"  
}  

## ⚙️ Tecnologias e Execução

O projeto é leve e utiliza apenas os recursos nativos da linguagem Python, garantindo máxima portabilidade.

### Tecnologias Utilizadas

  * **Linguagem:** Python 3.x
  * **Interface:** Console / Terminal
  * **Recursos:** Estruturas de dados nativas (`list`, `dict`) e módulo `os` para limpeza de tela.

### Como Iniciar o Sistema

Para rodar o projeto localmente, siga os passos abaixo:

1.  Certifique-se de ter o **Python 3** instalado na sua máquina.

2.  Clone o repositório ou baixe o arquivo `gerenciador_alunos.py`.

3.  Acesse a pasta do projeto no terminal.

4.  Execute o script principal:

    ```bash
    python gerenciador_alunos.py
    ```

-----

## 👤 Desenvolvedor

Este projeto foi desenvolvido por: **Janerson Alves**

  * *Data de Criação:* **03/12/2025**

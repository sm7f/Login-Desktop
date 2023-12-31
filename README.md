# Projeto Login em Python com PostgreSQL e Qt Designer

## Visão Geral
Este projeto é uma aplicação de login desenvolvida em Python que utiliza o banco de dados PostgreSQL para armazenar informações de usuários. A interface gráfica foi projetada utilizando o Qt Designer 5.15, proporcionando uma experiência interativa e visualmente agradável.

## Funcionalidades Principais
- **Cadastro de Usuários:** Permite o cadastro seguro de novos usuários no sistema.
- **Autenticação:** Verifica o nome de usuário e senha durante o processo de login.
- **Qt Designer 5.15:** Utiliza a ferramenta gráfica para criar uma interface intuitiva.

## Estrutura do Projeto
- **Register.py:** Contém a classe `Ui_Register` que define a interface gráfica e a função `validar_usuario` para o processo de cadastro e autenticação.
- **database.py:** Contém a classe `PDVClasse` responsável pela conexão ao banco de dados PostgreSQL e operações relacionadas.

## Como Utilizar
### Requisitos:
- Python
- PostgreSQL
- PyQt5

### Configuração:
1. Ajuste as informações de conexão ao banco de dados no arquivo `database.py`.

### Execução:
- Execute o arquivo `Login.py` para iniciar a aplicação de login.

## Como Contribuir
- Sinta-se à vontade para explorar o código, fazer melhorias ou corrigir problemas.
- Abra problemas (issues) para relatar bugs ou sugerir novas funcionalidades.
- Faça pull requests para contribuir diretamente para o desenvolvimento.

## Notas Importantes
- Certifique-se de seguir as boas práticas de segurança ao lidar com senhas e informações sensíveis.
- Mantenha a documentação atualizada para facilitar o entendimento e a colaboração.

<img src="https://i.ibb.co/0ZCb1cy/login.jpg" alt="login" border="0">

<img src="https://i.ibb.co/9c88VWV/register.jpg" alt="register" border="0">

import psycopg2
import logging


class PDVClasse:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            port="5432",
            database="Login",
            user="postgres",
            password="PoliSystemsapwd123"
        )

        

    def cadastrar_usuario(self, login, senha, senha_confirmacao):
        try:
            # Validar se as senhas correspondem
            if senha != senha_confirmacao:
                raise ValueError("As senhas não coincidem. Por favor, digite novamente.")

            cursor = self.conn.cursor()

            # Executar uma consulta SQL para inserir um novo usuário
            cursor.execute("INSERT INTO usuarios (login, senha) VALUES (%s, %s)", (login, senha))

            # Commit para efetivar a transação
            self.conn.commit()

            # Fechar o cursor
            cursor.close()

        except psycopg2.Error as e:
            logging.error(f"Ocorreu um erro ao cadastrar o usuário {login}: {e}")
            raise e
        except ValueError as ve:
            logging.error(f"Erro de validação: {ve}")
            raise ve

    def obter_usuarios(self):
        try:
            cursor = self.conn.cursor()

            # Executar uma consulta SQL para obter os dados da tabela usuarios
            cursor.execute("SELECT login, senha FROM usuarios")

            # Obter os resultados da consulta
            results = cursor.fetchall()

            # Fechar o cursor
            cursor.close()

            # Retornar os resultados
            return results

        except psycopg2.Error as e:
            logging.error(f"Ocorreu um erro ao obter os dados da tabela usuarios: {e}")
            raise e
        




    def verificar_credenciais(self, username, password):

        pdv = PDVClasse()


        try:
            # Criar um cursor para executar comandos SQL
            cursor = pdv.conn.cursor()

            # Executar uma consulta SQL para verificar as credenciais de login
            cursor.execute("SELECT * FROM usuarios WHERE login = %s AND senha = %s", (username, password))

            # Verificar se há algum resultado
            if cursor.fetchone():
                return True
            else:
                return False


        except psycopg2.Error as e:
            logging.error(f"Ocorreu um erro ao verificar as credenciais de login: {e}")
            raise e
        finally:
            # Fechar o cursor
            cursor.close()
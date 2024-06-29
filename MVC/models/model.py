import re
import requests
import mysql.connector
from mysql.connector import Error
import argon2

class ConexaoBanco:
    def __init__(self):
        self.base_url = 'https://economia.awesomeapi.com.br/last/'
        self.db_config = {
            'host': 'localhost',
            'port': '3306',
            'database': 'banco_de_dados',  # Nome do banco de dados
            'user': 'root',
            'password': 'aydon1234512345'
        }

    def conn_db(self):
        """Conectar ao banco de dados."""
        try:
            conn = mysql.connector.connect(**self.db_config)
            if conn.is_connected():
                return conn
        except Error as e:
            print("Erro ao conectar ao MySQL", e)
        return None
    
    def disconnect_db(self, conn):
        """Desconectar do banco de dados."""
        if conn.is_connected():
            conn.close()

class Usuario(ConexaoBanco):
    def __init__(self):
        super().__init__()

    def is_valid_email(self, email):
        """Validar formato de email."""
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    def is_valid_phone(self, phone):
        """Validar formato de telefone."""
        return re.match(r"^\d{10,15}$", phone) is not None

    def passwords_match(self, password, confirm_password):
        """Verificar se as senhas correspondem."""
        return password == confirm_password

    def validate_register_inputs(self, name, email, phone, password, confirm_password):
        """Validar campos de entrada de registro."""
        error_message = ""

        if not name:
            error_message += "Nome não pode estar vazio.\n"
        if not email or not self.is_valid_email(email):
            error_message += "Email inválido.\n"
        if not phone or not self.is_valid_phone(phone):
            error_message += "Telefone inválido. Deve conter apenas números e ter entre 10 e 15 dígitos.\n"
        if not password:
            error_message += "Senha não pode estar vazia.\n"
        if not confirm_password:
            error_message += "Confirme a senha não pode estar vazio.\n"
        if password and confirm_password and not self.passwords_match(password, confirm_password):
            error_message += "As senhas não correspondem.\n"

        return error_message

    def register_user(self, name, email, phone, password):
        """Registrar usuário no banco de dados."""
        conn = self.conn_db()
        if not conn:
            return "Erro ao conectar ao banco de dados."

        try:
            hashed_password = argon2.PasswordHasher().hash(password)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO usuario(nome, email, telefone, senha) VALUES (%s, %s, %s, %s)",
                (name, email, phone, hashed_password)
            )
            conn.commit()
            return "Usuário registrado com sucesso."
        except Error as e:
            return f"Erro ao registrar usuário: {e}"
        finally:
            self.disconnect_db(conn)

    def authenticate_user(self, email, password):
        """Autenticar usuário."""
        conn = self.conn_db()
        ph = argon2.PasswordHasher(
            time_cost=10,  
            memory_cost=65536,  
            parallelism=1,
            hash_len=32,
        )
        if not conn:
            return "Erro ao conectar ao banco de dados."

        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM usuario WHERE email = %s",
                (email,)
            )
            user = cursor.fetchone()

            if not user:
                return "Email ou senha incorretos."

            hashed_password = user[3]  

            if ph.verify(hashed_password, password):
                return user
            else:
                return "Email ou senha incorretos."
        except Error as e:
            return f"Erro ao autenticar usuário: {e}"
        finally:
            self.disconnect_db(conn)

    def validate_login_inputs(self, email, password):
        """Validar campos de entrada do login."""
        error_message = ""

        if not email or not self.is_valid_email(email):
            error_message += "Email inválido.\n"
        if not password:
            error_message += "Senha não pode estar vazia.\n"

        return error_message

class ConversorDeMoedas(ConexaoBanco):
    def __init__(self):
        super().__init__()
    
    def converter_valor(self, valor_entrada, moeda_de_valor, moeda_para_valor):
        url = f'{self.base_url}{moeda_de_valor}-{moeda_para_valor}'
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            taxa_cambio = float(data[f'{moeda_de_valor}{moeda_para_valor}']['bid'])
            valor_convertido = valor_entrada * taxa_cambio
            return valor_convertido
        except requests.exceptions.RequestException as e:
            raise Exception(f'Falha na requisição HTTP: {e}')
        except (KeyError, ValueError) as e:
            raise Exception(f'Erro ao processar resposta da API: {e}')

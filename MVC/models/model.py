import re
import requests

class Model:
    def __init__(self):
        self.base_url = 'https://economia.awesomeapi.com.br/last/'

    # Validação de email
    def is_valid_email(self, email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

    # Validação de telefone
    def is_valid_phone(self, phone):
        return re.match(r"^\d{10,15}$", phone)

    # Verificar se as senhas correspondem
    def passwords_match(self, password, confirm_password):
        return password == confirm_password

    # Validar todos os campos de entrada de registro
    def validate_register_inputs(self, name, email, phone, password, confirm_password):
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
            error_message += "Confirme a Senha não pode estar vazio.\n"
        if password and confirm_password and not self.passwords_match(password, confirm_password):
            error_message += "As senhas não correspondem.\n"

        return error_message

    # Validar campos de entrada do login
    def validate_login_inputs(self, email, password):
        error_message = ""

        if not email or not self.is_valid_email(email):
            error_message += "Email inválido.\n"
        if not password:
            error_message += "Senha não pode estar vazia.\n"

        return error_message

    # Converter moeda
    def converter_moeda(self, valor_entrada, moeda_de_valor, moeda_para_valor):
        url = f'{self.base_url}{moeda_de_valor}-{moeda_para_valor}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            taxa_cambio = float(data[f'{moeda_de_valor}{moeda_para_valor}']['bid'])
            valor_convertido = valor_entrada * taxa_cambio
            return valor_convertido
        else:
            raise Exception('Falha ao obter as taxas de câmbio. Tente novamente mais tarde.')

from models.model import Usuario, ConversorDeMoedas
from views.view import View

class Controller:
    def __init__(self, model):
        self.model = model
        self.conversor = ConversorDeMoedas()
        self.view = View(self)

    def valida_login(self):
        email = self.view.entry_email.get()
        senha = self.view.entry_senha.get()
        error_message = self.model.validate_login_inputs(email, senha)
        if error_message:
            self.view.error_label.config(text=error_message, fg="red")
        else:
            result = self.model.authenticate_user(email, senha)
            if isinstance(result, tuple):
                self.view.error_label.config(text="")
                self.view.open_conversor_window()
            else:
                self.view.error_label.config(text=result, fg="red")

    def open_registration_window(self):
        self.view.open_registration_window()

    def register(self, name, email, phone, password, confirm_password):
        error_message = self.model.validate_register_inputs(name, email, phone, password, confirm_password)
        if error_message:
            return error_message
        return self.model.register_user(name, email, phone, password)

    def converter(self):
        valor = self.view.entrada_valor.get()
        moeda_de = self.view.moeda_de.get()
        moeda_para = self.view.moeda_para.get()
        try:
            valor = float(valor)
            resultado = self.conversor.converter_valor(valor, moeda_de, moeda_para)
            self.view.app_resultado.config(text=f'{resultado:.2f}')
        except ValueError:
            self.view.app_resultado.config(text="Entrada de valor inválida")
        except Exception as e:
            self.view.app_resultado.config(text=str(e))

    def mostrar_historico(self):
        print("Aqui")
        try:
            historico_dados = self.conversor.obter_historico() 
            print(historico_dados)
            self.view.open_historico(historico_dados)  
        except Exception as e:
            print(f"Erro ao obter histórico: {e}")
            
            
   
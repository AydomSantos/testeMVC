from models.model import Model
from views.view import View
from tkinter import messagebox

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def valida_login(self):
        email = self.view.entry_email.get()
        password = self.view.entry_senha.get()
        error_message = self.model.validate_login_inputs(email, password)
        if error_message:
            self.view.error_label.config(text=error_message, fg="red")
        else:
            self.view.error_label.config(text="Login realizado com sucesso!", fg="green")
            print("Login realizado")
            self.view.open_conversor_window()

    def open_registration_window(self):
        self.view.open_registration_window()

    def converter(self):
        try:
            valor = float(self.view.entrada_valor.get())
            moeda_origem = self.view.moeda_de.get()
            moeda_destino = self.view.moeda_para.get()
            resultado = self.model.converter_moeda(valor, moeda_origem, moeda_destino)
            simbolo_destino = self.view.dict_moedas[moeda_destino]
            self.view.app_resultado.config(text=f"{simbolo_destino} {resultado:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um valor válido.")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

if __name__ == "__main__":
    app = Controller()
    app.view.start()

from models.model import Model
from views.view import View

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

    def open_registration_window(self):
        self.view.open_registration_window()

    

if __name__ == "__main__":
    app = Controller()
    app.view.start()

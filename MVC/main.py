
from tkinter import Tk
from controllers.controller import AuthController,PessoController  # Importe o controlador principal necessário
from views.view import View  # Importe sua classe View principal

def main():
    root = Tk()
    app = PessoController()
    view = View(app)
    view.start()  # Inicia a interface gráfica
    root.mainloop()

if __name__ == "__main__":
    main()

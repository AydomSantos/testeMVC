from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label, Toplevel
from tkinter import messagebox

class View:
    def __init__(self, controller):
        self.controller = controller
        self.window = Tk()
        self.window.geometry("800x800")
        self.window.configure(bg="#F39421")
        self.login_window()
        
    def relative_to_assets(self, path: str) -> str:
        from pathlib import Path
        script_dir = Path(__file__).parent
        assets_path = script_dir.parent / "assets" / "img_sistema"  # Corrigido para img_sistema
        return str(assets_path / path)
    
    def login_window(self):
        canvas = Canvas(
            self.window,
            bg="#F39421",
            height=800,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        # Add title text
        canvas.create_text(
            50.0,
            20.0,
            anchor="nw",
            text="Convertion Cash",
            fill="#FFFDFD",
            font=("MontserratItalic Medium", 48 * -1)
        )

        # Create entry fields
        self.entry_email = Entry(
            bd=0,
            bg="#FFFDFD",
            fg="#000716",
            highlightthickness=0,
            font=("Helvetica", 16)
        )
        self.entry_email.place(
            x=35.0,
            y=280.0,
            width=730.0,
            height=50.0
        )

        self.entry_senha = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Helvetica", 16),
            show="*"
        )
        self.entry_senha.place(
            x=35.0,
            y=380.0,
            width=730.0,
            height=50.0
        )

        # Add labels
        canvas.create_text(
            45.0,
            250.0,
            anchor="nw",
            text="Digite o seu email",
            fill="#FFFDFD",
            font=("Lato Medium", 24 * -1)
        )

        canvas.create_text(
            45.0,
            350.0,
            anchor="nw",
            text="Digite a sua senha",
            fill="#FFFDFD",
            font=("Lato Medium", 24 * -1)
        )

        # Add buttons
        button_img_login = PhotoImage(
            file=self.relative_to_assets("button_img_login.png")
        )
        button_login = Button(
            self.window,
            image=button_img_login,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.valida_login
        )
        button_login.place(
            x=250.8,
            y=460.0,
            width=278.0,
            height=78.0
        )

        button_img_register = PhotoImage(
            file=self.relative_to_assets("button_2.png")
        )
        button_register = Button(
            self.window,
            image=button_img_register,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.open_registration_window
        )
        button_register.place(
            x=250.0,
            y=600.0,
            width=278.0,
            height=78.0
        )

        # Add error label
        self.error_label = Label(
            self.window,
            text="",
            bg="#F39421",
            font=("Helvetica", 14)
        )
        self.error_label.place(
            x=35.0,
            y=700.0,
            width=730.0,
            height=50.0
        )

    def open_registration_window(self):
        register_window = Toplevel(self.window)
        register_window.geometry("800x800")
        register_window.configure(bg="#F39421")
        register_window.title("Cadastro")

        register_canvas = Canvas(
            register_window,
            bg="#F39421",
            height=800,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        register_canvas.place(x=0, y=0)

        register_canvas.create_text(
            50.0,
            20.0,
            anchor="nw",
            text="Cadastro",
            fill="#FFFDFD",
            font=("Montserrat Medium", 48)
        )

        fields = ["Nome", "Email", "Telefone", "Senha", "Confirme a Senha"]
        entry_fields = []
        for i, field in enumerate(fields):
            entry = Entry(
                register_window,
                bd=0,
                bg="#FFFDFD" if i != 2 else "#FFFFFF",
                fg="#000716",
                font=("Helvetica", 16),
                show="*" if "Senha" in field else ""
            )
            entry_fields.append(entry)

            register_canvas.create_text(
                45.0,
                110.0 + i * 100,
                anchor="nw",
                text=field,
                fill="#FFFFFF",
                font=("Lato Medium", 18)
            )

        def register():
            values = [entry.get() for entry in entry_fields]
            error_message = self.controller.model.validate_register_inputs(*values)

            if error_message:
                register_error_label.config(text=error_message, fg="red")
            else:
                register_error_label.config(text="Cadastro realizado com sucesso!", fg="green")
                print("Cadastro realizado")

        register_button = Button(
            register_window,
            text="Register",
            font=("Helvetica", 16),
            bg="#4CAF50",
            fg="white",
            borderwidth=0,
            highlightthickness=0,
            command=register
        )
        register_button.place(
            x=250.0,
            y=620.0,
            width=278.0,
            height=78.0
        )

        register_error_label = Label(
            register_window,
            text="",
            bg="#F39421",
            font=("Helvetica", 14)
        )
        register_error_label.place(
            x=35.0,
            y=710.0,
            width=730.0,
            height=50.0
        )

    def start(self):
        self.window.resizable(False, False)
        self.window.mainloop()

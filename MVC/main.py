from controllers.controller import Controller
from models.model import Usuario

if __name__ == "__main__":
    model = Usuario()
    app = Controller(model)
    app.view.start()
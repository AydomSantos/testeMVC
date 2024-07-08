from models.model import Pessoa, Conversao
from views.view import View

class AuthController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
    def valida_login(self):
        email = self.view.entry_email.get()
        senha = self.view.entry_senha.get()
        
        try:
            pessoa = self.model.buscar_pelo_email(email)
            
            if pessoa and self.verificar_senha(pessoa, senha):
                self.view.mostrar_mensagem('Login realizado com sucesso!')
                self.view.abrir_janela_conversor()
            else:
                self.view.mostrar_mensagem("Credenciais inválidas!")
        except Exception as e:
            self.view.mostrar_mensagem(f"Erro ao validar login: {str(e)}")
            
    def verificar_senha(self, pessoa, senha):
         return pessoa.senha == senha

class PessoController:
    def __init__(self, model, view):
        self.model = model
        self.view = view(self)
    
    def cadastrar_usuario(self, nome, email, telefone, senha):
        try:
            novo_usuario = Pessoa(nome=nome, email=email, telefone=telefone, senha=senha)
            self.model.cadastrar(novo_usuario)
            self.view.mostrar_mensagem('Usuário cadastrado com sucesso!')
        except Exception as e:
             self.view.mostrar_mensagem(f"Erro ao cadastrar usuário: {str(e)}")

    def abrir_janela_registro(self):
        self.view.abrir_janela_registro()

class ConversaoController:
    def __init__(self, conversor, view):
        self.conversor = conversor 
        self.view = view
        self.historico_dados = []
    
    def iniciar_aplicacao(self):
        # Lógica para iniciar a aplicação
        print("Aplicação iniciada")    
        
    def converter_moeda(self):
        valor = self.view.entrada_valor.get()
        moeda_origem = self.view.moeda_origem.get()
        moeda_destino = self.view.moeda_destino.get()
        
        try:
            valor = float(valor)
            resultado = self.conversor.converter_valor(valor, moeda_origem, moeda_destino)
            self.view.mostrar_resultado(resultado)
        except ValueError:
            self.view.mostrar_mensagem("Valor inválido para conversão!")
        except Exception as e:
            self.view.mostrar_mensagem(f"Erro na conversão de moeda: {str(e)}")
    
    def mostrar_historico_conversoes(self):
        try:
            self.historico_dados = self.conversor.obter_historico()
            self.view.mostrar_historico(self.historico_dados)
        except Exception as e:
            self.view.mostrar_mensagem(f"Erro ao obter histórico de conversões: {str(e)}")
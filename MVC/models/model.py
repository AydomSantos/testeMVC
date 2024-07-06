import sqlite3

class Pessoa():
    def __init__(self, nome, email, telefone, senha, id = None):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha = senha
        
    def cadastrar(self):
        conn = sqlite3.connect("conversor.db")
        cursor = conn.cursor()
        cursor.execute('insert into usuarios (nome, email, telefone, senha) values(?, ?, ?, ?)',(self.nome, self.email, self.telefone, self.senha))
        conn.commit()
        cursor.close()
        conn.close() 
         
    def editar(self):
        if self.id is None:
            raise ValueError("ID do usuário não especificado.")
        
        conn = sqlite3.connect("conversor.db")
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE usuarios
        SET nome = ?, email = ?, telefone = ?, senha = ?
        WHERE id = ?
        """, (self.nome, self.email, self.telefone, self.senha, self.id))
        conn.commit()
        cursor.close()
        conn.close()  
        
    def excluir(self):
        if self.id is None:
            raise ValueError("ID do usuário não especificado.")
        
        conn = sqlite3.connect("conversor.db")
        cursor = conn.cursor()
        cursor.execute('''
        'DELETE FROM usuarios WHERE id = ?'
        ''',(self.id,))
        conn.commit()
        cursor.close()
        conn.close()
            
        

# fazendo o cadastro do usuario

#pessoa_um = Pessoa("Duda", "dudu@gmail.com", 2451448541, "123")
#pessoa_um.cadastrar()

# ==============================================================

# faz a edição dos usuarios

# pessoa_um.id = 1
# pessoa_um.nome = "Aydom Atualizado"
# pessoa_um.email = "aydom@gmail.com"
# pessoa_um.telefone = 54785214785
# pessoa_um.senha = "senha atualizada"
# pessoa_um.editar()

# =================================================

class Conversor():
    def __init__(self, usuario, data_conversao, moeda_entrada, moeda_saida, valor_entrada, valor_saida, cotacao, id=None):
        self.id = id
        self.usuario = usuario
        self.data_conversao = data_conversao
        self.moeda_entrada = moeda_entrada
        self.moeda_saida = moeda_saida
        self.valor_entrada = valor_entrada
        self.valor_saida = valor_saida
        self.cotacao = cotacao
    def cadastrar(self):
        conn = sqlite3.connect("conversor.db")
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO conversoes(usuario, data_conversao, moeda_entrada, moeda_saida, valor_entrada, valor_saida, cotacao)
        VALUES(?, ?, ?, ?, ?, ?, ?)              
        ''', (self.usuario, self.data_conversao, self.moeda_entrada, self.moeda_saida, self.valor_entrada, self.valor_saida, self.cotacao))
        conn.commit()
        cursor.close()
        conn.close()
        
    def editar(self):
        conn = sqlite3.connect("conversor.db")
        cursor = conn.cursor()
        if self.id is None:
            raise ValueError("ID do usuário não especificado.")
        cursor.execute('''
        UPDATE conversoes usuario = ?, data_conversao = ?, moeda_entrada = ?, moeda_saida = ?, valor_entrada = ?, valor_saida = ?, cotacao = ?
        WHERE id = ?              
        ''',(self.usuario, self.data_conversao, self.moeda_entrada, self.moeda_saida, self.valor_entrada, self.valor_saida, self.cotacao, self.id))
        conn.commit()
        cursor.close()
        conn.close()
        

    def excluir(self):
        conn = sqlite3.connect("conversor.db")
        cursor = conn.cursor()
        if self.id is None:
            raise ValueError("ID do usuário não especificado.")
        cursor.execute('DELETE FROM usuarios WHERE id = ?', (self.id))
        conn.commit()
        cursor.close()
        conn.close()
        

# Criar uma nova conversão e cadastrá-la
conversao = Conversor("Usuário Teste", "2024-07-06", "USD", "BRL", 100.0, 500.0, 5.0)
conversao.cadastrar()
print("Conversão cadastrada.")

conversao.id = 1
conversao.usuario = "Usuário Atualizado"
conversao.data_conversao = "2024-07-07"
conversao.moeda_entrada = "EUR"
conversao.moeda_saida = "BRL"
conversao.valor_entrada = 200.0
conversao.valor_saida = 1000.0
conversao.cotacao = 5.0
conversao.editar()
print("Conversão editada.")


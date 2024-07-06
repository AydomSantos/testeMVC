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

pessoa_um = Pessoa("Duda", "dudu@gmail.com", 2451448541, "123")
#pessoa_um.cadastrar()

# ==============================================================

# faz a edição dos usuarios

pessoa_um.id = 1
pessoa_um.nome = "Aydom Atualizado"
pessoa_um.email = "aydom@gmail.com"
pessoa_um.telefone = 54785214785
pessoa_um.senha = "senha atualizada"
pessoa_um.editar()

# =================================================
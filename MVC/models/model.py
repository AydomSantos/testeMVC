import sqlite3

class Pessoa():
    def __init__(self, nome, email, telefone, senha, senha_hash, id = None):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha = senha
        self.senha_hash = senha_hash
        
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
    
    def buscar_pelo_email(self, email):
        try:
            conn = sqlite3.connect('conversor.db')  
            cursor = conn.cursor()       
            
            cursor.execute('SELECT id, nome, email, senha_hash FROM pessoas WHERE email = ?', (email,)) 
            result = cursor.fetchone()
            
            if result:
                pessoa = Pessoa(*result)
                return pessoa  
            else:
                return None
            
        except sqlite3.Error as e:
            print(f"Erro ao acessar SQLite: {e}")
            return None
        finally:
            cursor.close()
            conn.close()
            
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
        




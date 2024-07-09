import sqlite3
from typing import Optional

class Pessoa():
    def __init__(self, nome: str, email: str, telefone: str, senha: str,  id: Optional[int] = None):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha = senha
      
class PessoaRepository:       
    def cadastrar(self, pessoa: Pessoa) -> None:
        conn = sqlite3.connect("conversor.db")
        cursor = conn.cursor()
        cursor.execute('INSERT INTO usuarios (nome, email, telefone, senha) VALUES (?, ?, ?, ?)', (pessoa.nome, pessoa.email, pessoa.telefone, pessoa.senha))
        conn.commit()
        

            
    def editar(self, pessoa: Pessoa) -> None:
        conn = sqlite3.connect("conversor.db")
        cursor = conn.cursor()
        if pessoa.id is None:
            raise ValueError("ID do usuário não especificado.")
        
        cursor.execute("""
        UPDATE usuarios
        SET nome = ?, email = ?, telefone = ?, senha = ?
        WHERE id = ?
        """,(pessoa.nome, pessoa.email, pessoa.telefone, pessoa.senha))
        conn.commit()
        
    
    def excluir(self, pessoa: Pessoa) -> None:
        conn = sqlite3.connect("conversor.db")
        cursor = conn.cursor()
        if pessoa.id is None:
            raise ValueError("ID do usuário não especificado.")
        
        cursor.execute("""
          DELETE FROM usuarios WHERE id = ?', (pessoa.id,)             
        """)
        conn.commit()
        
    
    def pesquisar_por_email(self, email: str) -> Optional[Pessoa]:
        try:
            conn = sqlite3.connect('conversor.db')
            cursor = conn.cursor()
            
            cursor.execute('SELECT id, nome, email, telefone, senha, senha_hash FROM usuarios WHERE email = ?', (email,))
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
                
class Conversao():
    def __init__(self, usuario: str, data_conversao: str, moeda_entrada: str, moeda_saida: str, valor_entrada: float, valor_saida: float, cotacao: float, id: Optional[int] = None):
        self.id = id
        self.usuario = usuario
        self.data_conversao = data_conversao
        self.moeda_entrada = moeda_entrada
        self.moeda_saida = moeda_saida
        self.valor_entrada = valor_entrada
        self.valor_saida = valor_saida
        self.cotacao = cotacao
    
class ConversaoRepository:

    def cadastrar(self, conversor:Conversao) -> None:
        conn = sqlite3.connect('conversor.db')
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO conversoes (usuario, data_conversao, moeda_entrada, moeda_saida, valor_entrada, valor_saida, cotacao)
        VALUES (?, ?, ?, ?, ?, ?, ?)             
        """, (conversor.usuario, conversor.data_conversao, conversor.moeda_entrada, conversor.moeda_saida, conversor.valor_entrada, conversor.valor_saida, conversor.cotacao))
        conn.commit()      
    
    def editar(self, conversao: Conversao) -> None:
        if conversao.id is None:
            raise ValueError("ID do usuário não especificado.")
        conn = sqlite3.connect('conversor.db')
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE conversoes
        SET usuario = ?, data_conversao = ?, moeda_entrada = ?, moeda_saida = ?, valor_entrada = ?, valor_saida = ?, cotacao = ?
        WHERE id = ?                           
        """,(conversao.usuario, conversao.data_conversao, conversao.moeda_entrada, conversao.moeda_saida, conversao.valor_entrada, conversao.valor_saida, conversao.cotacao, conversao.id))
        conn.commit()
        
    
    def excluir(self, conversao: Conversao) -> None:
        if conversao.id is None:
            raise ValueError("ID do usuário não especificado.")
        conn = sqlite3.connect('conversor.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM conversoes WHERE id = ?', (conversao.id,))
        conn.commit()
        
    
    def historico_conversao(self, conversao: Conversao):
        conn = sqlite3.connect('conversor.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM conversoes WHERE id = ?', (conversao.id))
        cursor.fetchall()
        conn.commit()
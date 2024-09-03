from Banco import Banco

class Usuario:
    def __init__(self):
        self.banco = Banco()

    def inserir(self, nome, telefone, email, usuario, senha):
        cursor = self.banco.conexao.cursor()
        cursor.execute('''
            INSERT INTO usuarios (nome, telefone, email, usuario, senha)
            VALUES (?, ?, ?, ?, ?)
        ''', (nome, telefone, email, usuario, senha))
        self.banco.conexao.commit()

    def alterar(self, idUsuario, nome, telefone, email, usuario, senha):
        cursor = self.banco.conexao.cursor()
        cursor.execute('''
            UPDATE usuarios SET nome=?, telefone=?, email=?, usuario=?, senha=?
            WHERE idUsuario=?
        ''', (nome, telefone, email, usuario, senha, idUsuario))
        self.banco.conexao.commit()

    def excluir(self, idUsuario):
        cursor = self.banco.conexao.cursor()
        cursor.execute('DELETE FROM usuarios WHERE idUsuario=?', (idUsuario,))
        self.banco.conexao.commit()

    def buscar(self, idUsuario):
        print(f"Buscando usuário com ID: {idUsuario}")  # Mensagem de depuração
        cursor = self.banco.conexao.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE idUsuario=?', (idUsuario,))
        resultado = cursor.fetchone()
        print(f"Resultado da busca: {resultado}")  # Mensagem de depuração
        return resultado
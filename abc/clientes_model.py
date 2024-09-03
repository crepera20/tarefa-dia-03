from Banco import Banco

class Cliente:
    def __init__(self):
        self.banco = Banco()

    def inserir(self, nome, telefone, endereco):
        cursor = self.banco.conexao.cursor()
        cursor.execute('''
            INSERT INTO cliente (nome, telefone, endereco)
            VALUES (?, ?, ?)
        ''', (nome, telefone, endereco))
        self.banco.conexao.commit()

    def alterar(self, idcli, nome, telefone, endereco):
        cursor = self.banco.conexao.cursor()
        cursor.execute('''
            UPDATE cliente SET nome=?, telefone=?, endereco=?
            WHERE idcli=?
        ''', (nome, telefone, endereco, idcli))
        self.banco.conexao.commit()

    def excluir(self, idcli):
        cursor = self.banco.conexao.cursor()
        cursor.execute('DELETE FROM cliente WHERE idcli=?', (idcli,))
        self.banco.conexao.commit()

    def buscar(self, idcli):
        cursor = self.banco.conexao.cursor()
        cursor.execute('SELECT * FROM cliente WHERE idcli=?', (idcli,))
        return cursor.fetchone()

from Banco import Banco

class cidade:
    def __init__(self):
        self.banco = Banco()

    def inserir(self, nome, uf):
        cursor = self.banco.conexao.cursor()
        cursor.execute('''
            INSERT INTO cidade (nome, uf)
            VALUES (?, ?)
        ''', (nome, uf))
        self.banco.conexao.commit()

    def alterar(self, idCidade, nome, uf):
        cursor = self.banco.conexao.cursor()
        cursor.execute('''
            UPDATE cidade SET nome=?, uf=?
            WHERE idCidade=?
        ''', (nome, uf, idCidade))
        self.banco.conexao.commit()

    def excluir(self, idCidade):
        cursor = self.banco.conexao.cursor()
        cursor.execute('DELETE FROM cidade WHERE idCidade=?', (idCidade,))
        self.banco.conexao.commit()

    def buscar(self, idCidade):
        cursor = self.banco.conexao.cursor()
        cursor.execute('SELECT * FROM cidade WHERE idCidade=?', (idCidade,))
        return cursor.fetchone()

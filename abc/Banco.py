import sqlite3

class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.criar_tabelas()

    def criar_tabelas(self):
        cursor = self.conexao.cursor()

        # Criação da tabela usuarios
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                idUsuario INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                telefone TEXT,
                email TEXT,
                usuario TEXT UNIQUE,  -- Adicionado UNIQUE para evitar usuários duplicados
                senha TEXT
            )
        ''')

        # Criação da tabela cidade
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cidade (
                idCidade INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                uf TEXT
            )
        ''')

        # Criação da tabela cliente
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cliente (
                idcli INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT NOT NULL,
                endereco TEXT NOT NULL,
                cpf TEXT NOT NULL
            )
        ''')

        self.conexao.commit()

    def buscar_usuario(self, usuario):
        cursor = self.conexao.cursor()
        try:
            cursor.execute("SELECT * FROM usuarios WHERE usuario = ?", (usuario,))
            return cursor.fetchone()  # Retorna o primeiro resultado ou None se não houver resultados
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            return None

    def fechar_conexao(self):
        self.conexao.close()

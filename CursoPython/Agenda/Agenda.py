import sqlite3


class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, Nome, Telefone):
        consulta = 'INSERT OR IGNORE INTO agenda(Nome, Telefone) VALUES(?, ?)'
        self.cursor.execute(consulta, (Nome, Telefone))
        self.conn.commit()

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE OR IGNORE agenda SET Nome=?, Telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute("SELECT * FROM agenda")

        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        consulta = "SELECT * FROM agenda WHERE nome LIKE ?"
        self.cursor.execute(consulta, (f'%{valor}%',))

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()



if __name__ == "__main__":
    agenda = AgendaDB("agenda.db")
    agenda.excluir(2)
    agenda.listar()
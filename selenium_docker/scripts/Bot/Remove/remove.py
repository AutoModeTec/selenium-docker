# Classe responsavel por remover o usuario do DB
class removeUser:
    def __init__(self):
        self.number = None
        self.db = None

    # Função que busca o usuario e remove-o do DB
    def remove(self):
        cursor = self.db.cursor()
        comand_sql = f"DELETE FROM NumbersSend WHERE Number = {self.number}"
        cursor.execute(comand_sql)
        self.db.commit()
        return

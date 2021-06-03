# Classe responsavel por vereificar a existencvia do usuario no DB
class verificationExist:
    def __init__(self):
        self.number = None
        self.db = None

    # Função de verificação do usuario e de padronização do numero
    def verificarion(self):
        aux = 0
        auxNumber = ''
        # Percore o numero, a fim de remover o "+55"
        for i in self.number:
            if aux > 2:
                auxNumber += i
            aux += 1
        self.number = auxNumber

        # Busca o numero no DB
        cursor = self.db.cursor()
        comand_sql = f"SELECT * FROM NumbersSend WHERE Number = {self.number}"
        cursor.execute(comand_sql)
        reader = cursor.fetchall()

        # Verifica se foi encontrado alguma numero
        if len(reader) == 0:
            return False
        else:
            # Numero encontrado e retorna-o para o processo
            return self.number

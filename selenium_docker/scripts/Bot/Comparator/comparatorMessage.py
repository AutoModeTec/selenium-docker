from scripts.Bot.Send.feedbackDeveloper import feedBaksForDeveloper
from scripts.Bot.Send.sendMensage import joinConversation
from scripts.Bot.Verification.verificationUser import verificationExist
from scripts.Bot.Remove.remove import removeUser
import csv
import mysql.connector


# Classe responsavel por vereificar a existencvia do usuario no DB
class ComparationMsgUser:
    def __init__(self):
        self.message = None
        self.number = None
        self.driver = None

    # Função responsavel pela comparação da mensagem recebido do cliente com o banco de dados.
    def Comparation(self):
        # Faz a conecção com o banco de dados
        db = mysql.connector.connect(user='admin', password='Lg3botisaproduct',
                                     host='lg3bot.cxp5nvrsoub5.us-east-2.rds.amazonaws.com',
                                     database='lg3bot')

        # Abre e faz a leitura do arquivo com os padroes de resposta e armazen em um array
        cursor = db.cursor()
        sql1 = f"SELECT * FROM MessageClient WHERE Message='{self.message}'"
        cursor.execute(sql1)
        profile = cursor.fetchall()

        # Verifica se foi criada a necessidade de remoção do usuario do DB
        if len(profile) > 0:
            # Instancia a funções de envio de mensagem ao usuario
            send = joinConversation()
            send.driver = self.driver
            # Notifica o usuiario de sua remoção
            send.message = 'OK, seu numero foi retirado da lista de envio'
            send.SendMsg()

            # Chama uma função de vereificação da existencia do usuario no DB
            verification = verificationExist()
            verification.number = self.number
            verification.db = db
            numbers = verification.verificarion()

            # Verifica a existencia
            if self.number == numbers:
                # Chama a função de remoção
                remove = removeUser()
                remove.number = self.number
                remove.db = db
                remove.remove()
                return True
            else:
                # Instancia a funções de feedbacks
                notification = feedBaksForDeveloper()
                notification.driver = self.driver
                # Notifica os desenvolvedores da inexistencia do usuario
                notification.number = 'Numero do desenvolveror'
                notification.message = f'Numero {self.number} não esta no banco de dados'
                notification.sendFeedbak()
                return False
        else:
            return

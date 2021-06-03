from scripts.Bot.Verification.verificationMessage import VerifificationForAnswer
from scripts.Bot.Comparator.comparatorMessage import *
import time

# Para testar o bot individualmente descomente essas funções
'''from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(10)
execute = mainOfBot()
execute.driver = driver
execute.listNumber = ['+5562993189949']
execute.executBot()'''

# Classe responsavel por remover o usuario do DB
class mainOfBot:
    def __init__(self):
        self.driver = None
        self.listNumber = None

    # Função de controle das atividades do bot
    def executBot(self):
        # Instancia a funções de verificação das respostas dos usuarios
        verification = VerifificationForAnswer()
        verification.driver = self.driver
        # Percorre a lista de numeros chamndo as funções de veirficação e de comparação de resposta
        for number in self.listNumber:
            # Acessa a conversa do usuario para buscar sua resposta
            key = f'https://web.whatsapp.com/send?phone={number}&text='
            self.driver.get(key)
            time.sleep(4)

            # Chama as classes que selecionam a ultima mensagem da conversa e compara se existe correspondencia
            comparation = ComparationMsgUser()
            comparation.message = verification.verification()
            comparation.number = number
            comparation.driver = self.driver
            comparation.Comparation()
            return


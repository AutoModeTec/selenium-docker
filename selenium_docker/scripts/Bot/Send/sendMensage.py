from selenium.webdriver.common.keys import Keys
import time


# Classe reesponsavel pela função de envio de mensagem para o usuario
class joinConversation:
    def __init__(self):
        self.driver = None
        self.message = None

    # Função de envio de mensagem, pra o usuario que foi verificado
    def SendMsg(self):
        # Envia a mensagem
        campo_mensagem = self.driver.find_elements_by_xpath(
            '//div[contains(@class,"copyable-text selectable-text")]')
        campo_mensagem[1].send_keys(self.message)
        time.sleep(1)
        campo_mensagem[1].send_keys(Keys.ENTER)
        time.sleep(2)

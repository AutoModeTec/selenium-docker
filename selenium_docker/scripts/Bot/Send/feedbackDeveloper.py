import time
from selenium.webdriver.common.keys import Keys

# Classe resposavel pela função de envio de feedbacks para os desenvovedores e clientes via whatsapp
class feedBaksForDeveloper:
    def __init__(self):
        self.driver = None
        self.phone = None
        self.message = None

    # Função de envio 
    def sendFeedbak(self):
        # Responnsavel por encontra a conversa com o usuario e digitar a mensagem, isso ocorre via URL
        chave = f'https://web.whatsapp.com/send?phone={self.phone}&text={self.message}'
        self.driver.get(chave)
        time.sleep(5)
        try:
            # Verifica se o numero existe
            self.driver.find_elements_by_xpath('//div[contains(@class,"_3SRfO")]')[-1]
            return 1
        except:
            try:
                # Verifica se o mensagem foi digitada
                exist_mensagem = self.driver.find_elements_by_xpath(
                        '//div[contains(@spellcheck,"true")]')[-1].text
                if len(exist_mensagem) > 0:
                    # Envia a mensagem
                    campo_mensagem = self.driver.find_elements_by_xpath(
                        '//div[contains(@class,"copyable-text selectable-text")]')
                    campo_mensagem[1].send_keys(Keys.ENTER)
                    time.sleep(1) 
                    return 0
                else:
                    print('Erro (else')
            except:
                print('Erro')
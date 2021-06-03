import time


#Classe responsavel por verificar a existencia de notificações do usuario 
class VerifificationForAnswer:
    def __init__(self):
        self.driver = None

    # Verifica qual a ultima mensagem e o numero do usuario, caso exista é retornada para uma verificação.
    def Verifification(self):
        #Procura a localidade da mensagem, é encontrado um array com varios dados 
        location = self.driver.find_elements_by_xpath(
            '//div[contains(@class,"_1bR5a")]')[-1].location
        message = self.driver.find_elements_by_xpath(
            '//span[contains(@class,"selectable-text copyable-text")]')[-1].text

        #Separa apenas o parametro 'x' do array
        location = int(location['x'])

        # Usa a localização da mensagem para definir se a mensagem é do usuario ou do remetente
        if location < 650:
            message = message.lower()
            return message

        # Pega o numero do usuario na mensagem
        '''numero = self.driver.find_element_by_xpath('//div[contains(@class,"_2KQyF")]').text
        # Padroniza o numero
        numero = numero.replace(' ', '')
        numero = numero.replace('-', '')'''


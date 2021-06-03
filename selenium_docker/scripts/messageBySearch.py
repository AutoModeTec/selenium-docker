from selenium.webdriver.common.keys import Keys
import time


class SendMessage:
    def __init__(self, driver):
        self.driver = driver

    # uses the whatsapp's search bar to look for the contact chat
    def searh_contact(self, contact, time_plus):
        # for i in range(3):
        try:
            search_field = self.driver.find_element_by_xpath(
                '//div[contains(@class, "copyable-text selectable-text")]')
            search_field.click()
            if len(search_field.text) > 0:                    
                for x in range(30):
                    search_field.send_keys(Keys.BACKSPACE)
            search_field.send_keys(contact)
            time.sleep(1 + time_plus)
            search_field.send_keys(Keys.ENTER)
            time.sleep(1 + time_plus)
            # break
        except:
            raise ValueError('SendMessage.searh_contact')

    # function that actually send the message
    def send_message(self, contact, message, time_plus):
        campo_message = self.driver.find_elements_by_xpath(
            '//div[contains(@class,"copyable-text selectable-text")]')
        campo_message[1].send_keys(message)
        time.sleep(time_plus + 1)
        campo_message[1].send_keys(Keys.ENTER)
        time.sleep(time_plus + 1)

    # the general function that calls the other two above
    def send_text_written(self, contact, message, time_plus, aux=0):
        try:
            self.searh_contact(contact, time_plus)
        except:
            raise ValueError('SendMessage.send_text_written1')
        else:
            try:
                self.send_message(contact, message, time_plus)
            except:
                aux += 1
                time_plus += 3
                if aux < 3:
                    self.driver.get('https://web.whatsapp.com/')
                    self.send_text_written(contact, message, time_plus, aux)
                else:
                    raise ValueError('SendMessage.send_text_written2')

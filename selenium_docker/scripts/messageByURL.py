from selenium.webdriver.common.keys import Keys
import time
from scripts.failedNumbers import *
from scripts.AlreadySent import *


class NewContact:
    def __init__(self, driver):
        self.driver = driver
        self.time_plus = 0
 
    # function that receive the target
    def register(self, phone, message, driver):

        # sends messages to the target
        
        self.send(phone, message, driver)
        try:
            pass
        except:
            NonExistencePhone(phone)

    # function that actually send the message
    def send(self, phone, message, driver):
        try:
            path = f'https://web.whatsapp.com/send?phone=+55{phone}&text={message}'
            driver.get(path)
        except:
            self.send(phone, message, driver)

        try:
            time.sleep(5)
            # search for an error
            driver.find_elements_by_xpath('//div[contains(@class,"_3B-ht")]')[-1]

            NonExistencePhone(phone)

            # found an error
            time.sleep(3.5)
            return
        except:
            # send message
            message_field = driver.find_elements_by_xpath(
                '//div[contains(@class,"copyable-text selectable-text")]')[-1]
            message_field.send_keys(Keys.ENTER)
            # message_field.click()
            # message_field.click()
            # I sent a message

            # verificate if message wasn't sent
            if not AlreadySent(driver, message):
                self.send(phone, message, driver)
            time.sleep(6)

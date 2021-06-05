from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import mysql.connector
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options
from scripts.scrollChats import *
from scripts.Bot.mainForBot import *


db = mysql.connector.connect(user='admin', password='Lg3botisaproduct',
                             host='lg3bot.cxp5nvrsoub5.us-east-2.rds.amazonaws.com',
                             database='lg3bot')

chrome_options = Options()
chrome_options.add_argument('--disable-dev-shm-usage') 
chrome_options.add_argument('--no-sandbox')
try: 
    driver = Remote(command_executor='http://172.18.0.2:4444/wd/hub',
                     desired_capabilities={'browserName': 'chrome'}, options=chrome_options)
except:
    driver = Remote(command_executor='http://172.18.0.3:4444/wd/hub',
                     desired_capabilities={'browserName': 'chrome'}, options=chrome_options)

# updating the qrcode image
def send_image_to_db():
    blob_value = open('whatsappWeb.png', 'rb').read()
    sql = "UPDATE screenshot SET image=%s WHERE id=%s"
    Id = "1"
    args = (blob_value, Id)
    cursor = db.cursor()
    cursor.execute(sql, args)
    db.commit()


def verification():
    db = mysql.connector.connect(user='admin', password='Lg3botisaproduct',
                             host='lg3bot.cxp5nvrsoub5.us-east-2.rds.amazonaws.com',
                             database='lg3bot')
    cursor = db.cursor()
    sql1 = f"SELECT * FROM NumbersSend WHERE confirmation = 'f' "
    cursor.execute(sql1)
    df = cursor.fetchall()
    return df

def send(df, nc, message, driver):
    db = mysql.connector.connect(user='admin', password='Lg3botisaproduct',
                                 host='lg3bot.cxp5nvrsoub5.us-east-2.rds.amazonaws.com',
                                 database='lg3bot')
    # part in which the sending of messages occurs
    for number in df:
        nc.register(number[1], message, driver)

        cursor = db.cursor()
        sql = "UPDATE NumbersSend SET confirmation=%s WHERE id=%s"
        values = ('v', number[0])
        cursor.execute(sql, values)
        db.commit()
    return True

def WriteToDBForSend(nc, message, driver):
    db = mysql.connector.connect(user='admin', password='Lg3botisaproduct',
                                 host='lg3bot.cxp5nvrsoub5.us-east-2.rds.amazonaws.com',
                                 database='lg3bot')
    cursor = db.cursor()

    sqlbreak = f"SELECT * FROM NumbersSend WHERE confirmation = 'b' "
    cursor.execute(sqlbreak)

    df = cursor.fetchall()

    # condition that breaks the cycle
    if len(df) != 0:
        return False

    df = verification()

    # step that analyzes the responses with the bot
    if len(df) == 0:
        driver.get('https://web.whatsapp.com/')
        time.sleep(3)

        # HERE COMES THE LIST OF NUMBERS WITH MESSAGES
        numbers_list = scrollChats(driver)
        executBot = mainOfBot()
        executBot.driver = driver
        executBot.listNumber = numbers_list
        executBot.executBot()
        df = verification()
        if len(df) == 0:
            time.sleep(600)
        else:
            send(df, nc, message, driver)
        return True
    else:
        send(df, nc, message, driver)


# Function that checks and wait for the qr code verification to be done
def qrcode_step(driver, aux=0):
    qrcode = driver.find_elements_by_xpath(
        '//div[contains(@class,"_3jid7")]')

    if qrcode:
        if aux == 0 or aux == 3:
            driver.save_screenshot('whatsappWeb.png')
            send_image_to_db()
            aux = 0

    # wait for the qrcode to disappear
    try:
        WebDriverWait(driver, 10).until(EC.invisibility_of_element(
            (By.XPATH, '//div[contains(@class,"_3jid7")]')))
    except TimeoutException:
        try:
            a = driver.find_element_by_xpath('//div[contains(@class,"_2tiyK")]')
            a.click()
            aux = -1
            WebDriverWait(driver, 1).until(EC.element_to_be_clickable(
                (By.XPATH, '//div[contains(@class,"_2tiyK")]')))
        except NoSuchElementException:
            print('ainda nao apareceu botao reload')
        except TimeoutException:
            print('ainda nao apareceu botao reload2')
        finally:
            aux += 1
            qrcode_step(driver, aux)

    finally:
        print('imagem do qrcode SUMIO')

    return 0


def main(message, driver):
    print('main')
    driver.get('https://web.whatsapp.com/')
    time.sleep(10)

    driver.save_screenshot('whatsappWeb.png')
    print("screenshot")
    send_image_to_db()
    print("send_to_db")
    time.sleep(30)
    # qrcode verification step
    print("qrcode_step")
    qrcode_step(driver)
    print("New contact")
    nc = NewContact(driver)

    time.sleep(3)
    # cycle in which the program reads and writes to the database
    print("while true")
    while True:
        breaker = WriteToDBForSend(nc, message, driver)
        if not breaker:
            break


if __name__ == '__main__':
    message = 'Eu nao espero que você tenha um belo anoitecer e que descanse sorrindo.'
    main(message, driver)
    driver.close()

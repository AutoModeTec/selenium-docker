from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException


def AlreadySent(driver, message):
    messageField = driver.find_elements_by_xpath(
        '//span[contains(@class,"_3-8er selectable-text copyable-text")]')[-1]

    try:
        WebDriverWait(driver, 1).until(EC.visibility_of(
            messageField))
        if message in messageField.text:
            # message is the same on both
            return True
        else:
            # message isn't the same
            return False

    except TimeoutException:
        # can't find the element
        return False

    except NoSuchElementException:
        # can't find element
        return False

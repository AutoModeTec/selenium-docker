from scripts.messageByURL import *


def listSort(numbers_list):
    # bubble sort
    ordered = False
    while not ordered:
        ordered = True
        for i in range(len(numbers_list)-1):
            if int(numbers_list[i][1][:2]) > int(numbers_list[i+1][1][:2]):
                numbers_list[i], numbers_list[i+1] = numbers_list[i+1], numbers_list[i]
                ordered = False
            elif int(numbers_list[i][1][:2]) == int(numbers_list[i+1][1][:2]):
                if int(numbers_list[i][1][3:]) > int(numbers_list[i + 1][1][3:]):
                    numbers_list[i], numbers_list[i+1] = numbers_list[i+1], numbers_list[i]
                    ordered = False
    return numbers_list


def scrollChats(driver, contact_old='', numbers_list=None):

    if numbers_list is None:
        numbers_list = []

    recentList = driver.find_elements_by_xpath("//div[@class='_2aBzC']")
    contact = []

    for chat in recentList:
        try:
            driver.execute_script("arguments[0].scrollIntoView();", chat)
            contact = chat.text
            contact = contact.split('\n')
        except:
            pass
        try:
            # check if the chat has a new message
            if contact[3]:
                numbers_list.append((contact[0], contact[1]))
                try:
                    numbers_list = listSort(numbers_list)
                except:
                    pass
        except:
            pass
        time.sleep(1)
    try:
        # check if the analyzed chat has already been analyzed before
        if contact == contact_old:
            return numbers_list
        else:
            contact_old = contact
            numbers_list = scrollChats(driver, contact_old, numbers_list)
            return numbers_list
    except:
        return numbers_list

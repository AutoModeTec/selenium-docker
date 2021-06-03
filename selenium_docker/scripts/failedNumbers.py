import mysql.connector


db = mysql.connector.connect(user='admin', password='Lg3botisaproduct',
                               host='lg3bot.cxp5nvrsoub5.us-east-2.rds.amazonaws.com',
                               database='lg3bot')


def NonExistencePhone(number):
    cursor = db.cursor()
    command_SQL = f"INSERT INTO InvalidNumbers (numbers) VALUES({number})"
    cursor.execute(command_SQL)
    db.commit()


def errorInSending(number):
    cursor = db.cursor()
    command_SQL = f"INSERT INTO ErrorSend (numbers) VALUES({number})"
    cursor.execute(command_SQL)
    db.commit()

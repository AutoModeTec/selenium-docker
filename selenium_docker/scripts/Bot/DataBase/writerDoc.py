import mysql.connector

# Função que adiciona novas mensagens ao DB de comparação
db = mysql.connector.connect(user='admin', password='Lg3botisaproduct',
                             host='lg3bot.cxp5nvrsoub5.us-east-2.rds.amazonaws.com',
                             database='lg3bot')


def generatorTable():
    cursor = db.cursor()
    sql1 = "CREATE TABLE  MessageClient  (ID int NOT NULL AUTO_INCREMENT,Message text,PRIMARY KEY (id))"
    cursor.execute(sql1)


def addData(Message):
    cursor = db.cursor()
    sql1 = f"INSERT INTO  MessageClient (Message) Value('{Message}')"
    cursor.execute(sql1)
    db.commit()


data = 'a'
cursor = db.cursor()
sql1 = f"SELECT * FROM MessageClient WHERE Message='{data}'"
datas = 'sair'
cursor.execute(sql1)
profile = cursor.fetchall()
print(len(profile))

# generatorTable()




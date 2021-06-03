import xlrd
import xlwt
import os
import pandas.io.sql as sql
from configparser import ConfigParser
import mysql.connector


db = mysql.connector.connect(user='admin', password='Lg3botisaproduct',
                               host='lg3bot.cxp5nvrsoub5.us-east-2.rds.amazonaws.com',
                               database='lg3bot')


def WriteToExcel():
    nametable = input('Qual nome da tabela: ')
    nomearquivo = input('Qual nome do arquivo a ser criado: ')
    rootPath = os.getcwd()
    rootPath = rootPath + "/excelFolder/ExcelNumbersList.xlsx"

    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet("mysheet1", cell_overwrite_ok=True)
    worksheet.Title = "Numbers List"

    df = sql.read_sql(f'SELECT id, numbers  FROM {nametable}', db)
    df.to_excel(f'{nomearquivo}.xls')

    print("Successfully created excel file")


WriteToExcel()

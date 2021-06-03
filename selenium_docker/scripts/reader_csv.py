import pandas as pd


def reader_csv(file):
    try:
        try:
            path = 'C:/Users/User/Downloads/' + file
            arquive = pd.read_csv(path, header=None, sep=',')
        except:
            # print('\033[31mErro ao localizar o arquivo!\033[m')
            pass
        else:
            # adding column name to the respective columns
            arquive.columns = ['Número']
    except:
        try:
            path = 'C:/Users/User/Downloads/' + file
            arquive = pd.read_csv(path, header=None, sep=';')
        except:
            # print('\033[31mErro ao localizar o arquivo!\033[m')
            pass
        else:
            # adding column name to the respective columns
            arquive.columns = ['Número']

    return arquive['Número']


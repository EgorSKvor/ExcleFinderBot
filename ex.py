import pandas as pd
xlsx = pd.ExcelFile('./БД школа.xlsx')
df = pd.read_excel(xlsx, 'Sheet1')


def search_pass_name(name: str):
    row_num = 0
    for idx in df.index:
        row_num += 1
        if df['ФИО'].loc[idx] == name:
            break
    # row_num - 1 потому что обращение по индексу
    return df['Пароль'].loc[row_num-1]


def search_pass_id(id: int):
    row_num = 0
    for idx in df.index:
        row_num += 1
        if df['Номер студенческого'].loc[idx] == id:
            break
    return df['Пароль'].loc[row_num-1]


# print(search_pass_name('Иванов Иван Иванович'))
# print(search_pass_id(424346346))

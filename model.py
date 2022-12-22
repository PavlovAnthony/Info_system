import csv
import file_creating
from os.path import exists
# поиск последнего ID
def findID():
    path = 'book.csv'
    valid = exists(path)
    if not valid:
        file_creating.csv_creating()
        return 0
# Если файл уже есть
    else:    
        with open ('book.csv', 'r',encoding = 'utf-8 ') as f:
                     
             reader = csv.DictReader(f)
             lastId=list(reader)[-1]["Id"]
             return  int(lastId)  
             
#поиск сотрудника
def searchByName(base, cont):
    name = input(f'Введите {cont}\n')
    flag= True
    results= []

    for row in base:
        if name ==row[cont]:
            flag=False
            results.append(row)
    if flag:
            results.append(f'{cont} |{name}| не найден')
    return results




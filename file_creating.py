import csv
def csv_creating ():
    file = 'book.csv'
    with open (file, 'w', encoding = 'utf-8') as data:
        header = ["Id","Фамилия", "Имя" , "Номер телефона", "Должность", "E-mail"]
        writer = csv.DictWriter(data, fieldnames=header)
        writer.writeheader()
        
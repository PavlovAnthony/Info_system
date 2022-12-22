
import csv
import os
def add_new(contact):
    with open ('book.csv', 'a',encoding = 'utf-8 ') as f:
            
            writer = csv.writer(f, delimiter=',')
            
            writer.writerows([contact.split(' || ')])
            
 
def get_base():
    
    csv_file = csv.DictReader(open ('book.csv', 'r', encoding = 'utf-8'))
    return csv_file

def del_string(Id):
   
    file = 'book2.csv'
    with open ('book.csv', 'r', encoding = 'utf-8') as f:
        csv_file = csv.DictReader(f)
   
        with open (file, 'w', encoding = 'utf-8') as data:
            header = ["Id","Фамилия", "Имя" , "Номер телефона", "Должность", "E-mail"]
            writer = csv.DictWriter(data, fieldnames=header)
            writer.writeheader()
            for row in csv_file:
                if Id !=row["Id"]:
                    writer.writerow(row) 
    
    os.remove("book.csv")
    os.rename('book2.csv', 'book.csv')   
    
def change_str(id_num, new_value):
    file = 'book2.csv'
    with open ('book.csv', 'r', encoding = 'utf-8') as f:
        csv_file = csv.DictReader(f)

        with open (file, 'w', encoding = 'utf-8') as data:
            header = ["Id","Фамилия", "Имя" , "Номер телефона", "Должность", "E-mail"]
            writer = csv.DictWriter(data, fieldnames=header, delimiter=',')
            
            writer.writeheader()
            for row in csv_file:
                if id_num !=row["Id"]:
                    writer.writerow(row)
                elif id_num ==row["Id"]:
                    writer.writerow(new_value)
    os.remove("book.csv")
    os.rename('book2.csv', 'book.csv')

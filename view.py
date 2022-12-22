

def choose_mode():
    return input('''Введите режим работы : 
                 1- добавление записи 
                 2 - поиск 
                 3 - удаление записи
                 4 - редактирование
                 ''')

def contact_to_s():
    return input('''Введите информацию для поиска записи:
                  Поиск по Фамилия - 1
                  Поиск по Имя - 2
                  Поиск по Номер телфона - 3
                  Поиск по Должность -4
                  
                  ''')

def new_contact(Id):
    
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    position = input('Введите должность: ')
    email = input('Введите E-mail: ')
        
    return f'{Id} || {last_name} || {first_name} || {phone_number} || {position} || {email}'

def show_found(result):
    print ('Результаты поиска: ')
    for i in result:
        print(i)
def correction():
    id_num = input('введите Id записи:  ')
    return id_num
def del_str():
    str = input('Удалить эту запись y/n?    ')
    return str

def change_cont(Id):
   
        
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    position = input('Введите должность: ')
    email = input('Введите E-mail: ')
    res = {'Id': Id, 'Фамилия': last_name, 'Имя': first_name, 'Номер телефона': phone_number, 'Должность': position, 'E-mail': email  }    
    return res        
def change_inp():
    str = input('Найдена 1 запись,редактировать? y/n')
    return str
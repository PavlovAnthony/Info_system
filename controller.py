import logger
import view
import model

Id = 0
choose=0      
def run():
    while True:
        mode = view.choose_mode()
        if mode == '1':
            Id = model.findID()
            Id += 1
            contact = view.new_contact(Id)
            logger.add_new(contact)
        elif mode == '2':
            result=find_person()
            view.show_found(result)
        elif mode == '3': 
             result=find_person()
             view.show_found(result)
             if 'не найден' not in result[0] and len(result)>1:
                id_num = view.correction()
                if view.del_str()=='y':
                    logger.del_string(id_num)
             elif 'не найден' not in result[0] and len(result)==1:
                
                id_num=list(result)[-1]["Id"]
                if view.del_str()=='y':
                    
                    logger.del_string(id_num)
        elif mode == '4': 
            result=find_person()
            view.show_found(result)
            if 'не найден' not in result[0] and len(result)>1:
                id_num = view.correction()
                new_value=view.change_cont(id_num)
                logger.change_str(id_num,new_value)
            elif 'не найден' not in result[0] and len(result)==1:
                id_num=list(result)[-1]["Id"]
                if view.change_inp()=='y':
                    new_value=view.change_cont(id_num)
                    logger.change_str(id_num,new_value)
                
def find_person():
    choose = view.contact_to_s()
    base = logger.get_base()
    if choose == '2':
                cont="Имя"
                result= model.searchByName(base, cont)
    elif choose == '1':
                 cont="Фамилия"
                 result= model.searchByName(base, cont)
    elif choose == '3':
                 cont="Номер телефона"
                 result= model.searchByName(base, cont)
    elif choose == '4':
                 cont="Должность"
                 result= model.searchByName(base, cont)                 
    return result
"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    dict_1 = {'Как дела?':'Хорошо!', 'Что делаешь?':'Программирую', 'Продашь почку?': 'Нет'}
    dict_2 = {'Как дела? ':'Хорошо!', 'Что делаешь? ':'Программирую', 'Продашь почку?' : 'Нет'}
    dict_3 = {'как дела?':'Хорошо!', 'что делаешь?':'Программирую', 'продашь почку?': 'Нет'}
    dict_4 = {'Как дела ':'Хорошо!', 'Что делаешь ':'Программирую', 'Продашь почку' : 'Нет'}
    dict_5 = {'как дела':'Хорошо!', 'что делаешь':'Программирую', 'продашь почку': 'Нет'}
    while True:
      try:
        question = input('Введите вопрос:\n')
        if question in dict_1:                 
            print (dict_1.get(question))       
            break
        elif question in dict_2:                 
            print (dict_2.get(question))       
            break
        elif question in dict_3:                 
            print (dict_3.get(question))       
            break
        elif question in dict_4:                 
            print (dict_4.get(question))       
            break
        elif question in dict_5:                 
            print (dict_5.get(question))       
            break  
        else:
            print ('Что за вопросы? Зайди нормально.')
      except (KeyboardInterrupt):
            print('Пока!')
            break
           
ask_user()

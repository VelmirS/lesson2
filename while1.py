"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""

def ask_user():
  while True:
    user_input = input('Как дела?\n')

    if user_input == 'Хорошо':
       return ('Если у вас все хорошо, то это супер. Прекрасного дня!')
       break           

result_ask = ask_user()

print(result_ask)

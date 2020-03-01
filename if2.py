"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def string_comparison(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        result = 0
    elif str1 == str2:
        result = 1
    elif len(str1) > len(str2):
        if str2 == 'learn':
            result = 3
        else:
            result = 2
    else:
        result = 'Nope!'
    return result


print(string_comparison('string number one', 1234))
print(string_comparison('helloworld', 'helloworld'))
print(string_comparison('this is a veeeery long string', 'and this is not'))
print(string_comparison('string number seven', 'learn'))
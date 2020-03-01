"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

classes_scores = [{'school_class': '1a', 'scores': [3, 4, 4, 5, 2]},
                  {'school_class': '2a', 'scores': [5, 4, 3, 5, 4]},
                  {'school_class': '2b', 'scores': [5, 3, 3, 5, 2]},
                  {'school_class': '3a', 'scores': [2, 4, 3, 3, 5]},
                  {'school_class': '4a', 'scores': [5, 5, 5, 5, 4]},
                  {'school_class': '4b', 'scores': [3, 3, 5, 5, 2]}]


def average_value(values):
    values_list = []
    for value in values:
        values_list.append(value)
    result = sum(values_list) / len(values_list)
    return round(result, 2)


all_scores_in_school = []
for classes in classes_scores:
    scores = classes['scores']
    all_scores_in_school = all_scores_in_school + scores
result_for_school = average_value(all_scores_in_school)
print('The average score in all school:', result_for_school)

for each_class in classes_scores:
    result_for_class = average_value(each_class['scores'])
    print('The average score in class', each_class['school_class'] + ':', result_for_class)

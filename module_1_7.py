# Дополнительное задание Модуль 1
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# рассчет средних оценок
average = [sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]), sum(grades[2]) / len(grades[2]),
           sum(grades[3]) / len(grades[3]), sum(grades[4]) / len(grades[4])]
# print ('Средние оценки:', average)

# сортировка списка студентов
sorted_student = sorted(students)
# print ('Список студентов:', sorted_student)

# заполнение журнала
journal = {}
journal.update({sorted_student[0]: (average[0]), sorted_student[1]: (average[1]), sorted_student[2]: (average[2]),
                sorted_student[3]: (average[3]), sorted_student[4]: (average[4])})
print('Журнал оценок:', journal)

# Дополнительное задание Модуль 1
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# рассчет средних оценок
grades0 = grades[0]
average0 = (int(sum(grades0)) / (len(grades0)))
grades1 = grades[1]
average1 = (int(sum(grades1)) / (len(grades1)))
grades2 = grades[2]
average2 = (int(sum(grades2)) / (len(grades2)))
grades3 = grades[3]
average3 = (int(sum(grades3)) / (len(grades3)))
grades4 = grades[4]
average4 = (int(sum(grades4)) / (len(grades4)))
#print ('Средние оценки:',  (average0), (average1), (average2), (average3), (average4))
# сортировка списка студентов
sorted_student = sorted (students)
#print ('Список студентов', sorted_student)
# заполнение журнала
journal = {}
journal.update ({sorted_student[0]:(average0), sorted_student[1]:(average1), sorted_student[2]:(average2), sorted_student[3]:(average3), sorted_student[4]:(average4)})
print ('Журная оценок', journal)

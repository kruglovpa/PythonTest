# Форматирование строк
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451

print('В команде Мастера кода участников: %s' % team1_num, '!')
print('Итого сегодня в командах участников: %s' % team1_num, 'и %s' % team2_num, '!')

print('Команда Волшебники данных решила задач: {} !'.format(score_2))
print('Волшебники данных решили задачи за {} c !'.format(team1_time))

print(f'Команды решили {score_1} и {score_2} задач.')

name_1= 'Мастера кода'
name_2 = 'Волшебники данных'
challenge_result = ''
if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = name_1
elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = name_2
else:
    challenge_result = 'сегоня у нас ничья'
print(f'Результат битвы: победа команды {challenge_result} !')

tasks_total = score_1 + score_2
time_avg = (team1_time + team1_time) / tasks_total
print(f'Сегодня было решено {tasks_total} задач, в среднем по {round(time_avg, 2)} секунды на задачу!')

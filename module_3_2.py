# Способы вызова функции
def send_email(message, recipient, sender='university.help@gmail.com'):
    true_adres = False

    if '@' in recipient and '@' in sender:
        if recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net'):
            if sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net'):
                true_adres = True
    if true_adres == False:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    if true_adres == True and sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    if true_adres == True and sender != recipient and sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
    if true_adres == True and sender != recipient and sender != 'university.help@gmail.com':
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

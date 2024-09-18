# Способы вызова функции
def send_email(message, recipient, *, sender='university.help@gmail.com'):
    domain_list = ['.com', '.ru', '.net']
    true_domain1 = False
    true_domain2 = False
    true_ad = False

    for i in domain_list:
        if recipient.endswith(i):
            true_domain1 = True
            break
    for i in domain_list:
        if sender.endswith(i):
            true_domain2 = True
            break
    if '@' in recipient and '@' in sender:
        true_ad = True

    if true_domain1 == true_domain2 == true_ad == True:
        if sender == recipient:
            print('Нельзя отправить письмо самому себе!')
        elif sender == 'university.help@gmail.com':
            print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
        else:
            print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)
    else:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

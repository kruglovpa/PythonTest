# Способы вызова функции
def send_email(message, recipient, sender='university.help@gmail.com'):
    domain = ['.com', '.ru', '.net']
    if '@' in recipient and '@' in sender:
        print('@ Ok')
    for i in domain:
        if domain[i] in recipient:
            print('domain recipient Ok')
    if domain[i] in sender:
        print('domain sender Ok')
    else:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    # elif sender == recipient:
    #     print('Нельзя отправить письмо самому себе!')
    # else:
    #     print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

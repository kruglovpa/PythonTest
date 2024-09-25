# Рекурсия
def get_multiplied_digits(number):
    str_number = str(number).strip('0')
    first = int(str_number[0])

    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


primer = get_multiplied_digits(402030)
print(primer)

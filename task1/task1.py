""" Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY 
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна. 
Для простоты договоримся, что год может быть в диапазоне [1, 9999]. Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
Проверку года на високосность вынести в отдельную защищённую функцию.
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку. """



def conversion_string_to_list(date_str: str) :
    DELIMITER = ['.', ':', '-']
    for elem in DELIMITER:  
        date_list = date_str.split(elem)
        if len(date_list) == 1:
            continue
        else:
            date_list = list(map(int, date_list))
            return date_list
    return False

def leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False


def date_func(date_str) -> bool:
    date_list = conversion_string_to_list(date_str)
    if date_str is False:
        return False
    if date_list[0] not in range(1, 32) or date_list[1] not in range(1, 13) or date_list[2] not in range(1, 10000):
        return False
    leap = leap_year(date_list[2])
    if date_list[1] < 8 and date_list[1] % 2 != 0:
        return True
    elif date_list[1] < 8:
        if leap and date_list[1] == 2 and date_list[0] in range(1, 30):
            return True
        elif date_list[1] == 2 and date_list[0] in range(1, 29):
            return True
        elif date_list[0] in range(1, 31):
            return True
        else:
            return False
    elif date_list[1] > 7 and date_list[1] % 2 == 0:
        return True
    elif date_list[1] > 7 and date_list[1] % 2 != 0 and date_list[0] in range(1, 31):
        return True
    else:
        return False
import urllib.request
import json

class PhoneNumber:
    def __init__(self):
        yellow = "\033[33m"
        red = "\033[31m"
        reset = "\033[0m"
        phone = input('''\n {}[+] Введите номер телефона{}\n(Пример '9111XXXXXXXX' '7495XXXXXXX'): '''.format(yellow, reset))
        getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=" + phone
        try:
            infoPhone = urllib.request.urlopen( getInfo )
            infoPhone = json.load(infoPhone)
            print('\n ' + '=' * 50)
            print('                    {}Результаты:{}\n'.format(yellow, reset))
            print(u" Номер сотового --->", "+" + phone)
            print(u" Страна ---> ", infoPhone["country"]["name"])
            print(u" Регион ---> ", infoPhone["region"]["name"])
            print(u" Город ---> ", infoPhone["0"]["name"])
            print(u" Округ ---> ", infoPhone["region"]["okrug"])
            print(u" Оператор ---> ", infoPhone["0"]["oper"])
            print(u" Часть света ---> ", infoPhone["country"]["location"])
            print(' ' + '=' * 50)

        except:
            print( "\n{}[!] - Phone not found - [!]{}\n".format(yellow, reset))
            print(' ' + '=' * 50)

        input('{}\n  [+] Нажмите ENTER, чтобы вернуться в главное меню{}'.format(red, reset))

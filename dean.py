import time
from colorama import init, Style

import social_deanon as sd
import ipdean as ipd, phonenum as phn

init()

resetstyle = Style.RESET_ALL
red = "\033[31m"
yellow = "\033[33m"
blue = "\033[34m"
reset = "\033[0m"

def logo():
    logo_text = """{}
  ____  _____    _    _   _  ___  _   _ 
 |  _ \| ____|  / \  | \ | |/ _ \| \ | |
 | | | |  _|   / _ \ |  \| | | | |  \| |
 | |_| | |___ / ___ \| |\  | |_| | |\  |
 |____/|_____/_/   \_\_| \_|\___/|_| \_|                             
    {}""".format(blue, reset)

    for line in logo_text.split('\n'):
        print(line)
        time.sleep(0.1)

    print(Style.BRIGHT + 'Loading...' + resetstyle)
    time.sleep(2)


def menu():
    while True:
        print('''{}                                               
 .___.    __.  .______.  .____. ._.  ._.  ._.  
 |    \  /  |  |   ___|  |    \ | |  |  | | | 
 |     \/   |  |   ___|  |     \| |  |  |_| | 
 |__/\__/|__|  |______|  |__/\____|  |______| 
{}'''.format(yellow, reset))
        print(' {}{}ГЛАВНОЕ МЕНЮ{}{}\n 1) Проверка по нику\n 2) Проверка по IP-адресу \n 3) Проверка по номеру телефона'.format(Style.BRIGHT, yellow, reset, resetstyle))
        print(' 0) ! ВЫХОД !')
        home_page = int(input('\n {}[+] Cделайте выбор: {}'.format(yellow, reset)))

        if home_page == 0:
            print('\n {}{}До свидания!{}{}'.format(Style.BRIGHT, blue, reset, resetstyle))
            break
        elif home_page == 1:
            sd.SocialDeanon()
        elif home_page == 2:
            ipd.Ipcheck()
        elif home_page == 3:
            phn.PhoneNumber()
        else:
            print(' {}Введите существующий пункт меню!{}'.format(red, reset))
            continue


if __name__ == '__main__':
    logo()
    menu()
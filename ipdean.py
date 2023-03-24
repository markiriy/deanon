import requests
import sys


class Ipcheck:
    def __init__(self):
        red = "\033[31m"
        green = "\033[32m"
        yellow = "\033[33m"
        blue = "\033[34m"
        reset = "\033[0m"
        try:
            self.inputip = input('\n{} [+] Введите IP-адрес{}\n(Если вы хотите проверить собственный IP, нажмите ENTER):'.format(yellow, reset))
        except ValueError:
            raise ValueError('{}IP адресс введён неверно{}'.format(red, reset))
        except KeyboardInterrupt:
            print("{}\n\tYou have terminated the program. Please re-run to access your ip address{}".format(red,
                                                                                                            reset))
        except requests.ConnectionError:
            print("{}\n\t\tYou are not properly connected to the internet\n{}".format(blue, reset))
        except requests.HTTPError:
            print("{}\n\tSORRY{} {}You have exceeded your daily limit{}\n".format(red, reset, yellow,
                                                                                  reset))
        except requests.ConnectTimeout:
            print("{}\n\tConnection to the server has timed out{}\n".format(green, reset))
        except requests.ReadTimeout:
            print("{}\n\tThe Server failed to send the required data. Reload to solve problem{}\n".format(red,
                                                                                                          reset))
        except requests.exceptions.JSONDecodeError:
            print("{}\n\tWrong input. Expected: XXX.XXX.XXX.XXX{}\n".format(red, reset))
        self.ConnectionStart(self.inputip)
        self.Pretty()
        input('{}\n  [+] Нажмите ENTER, чтобы вернуться в главное меню{}'.format(red, reset))

    def ConnectionStart(self, ip):
        req = requests.request('get', f"http://free.ipwhois.io/json/{ip}", timeout=1.5).json()
        global inow
        inow = dict(req)

    def Pretty(self):
        red = "\033[31m"
        yellow = "\033[33m"
        blue = "\033[34m"
        reset = "\033[0m"

        ip = inow['ip']
        country = inow['country']
        isp = inow['isp']
        city = inow['city']
        latitude = inow['latitude']
        longitude = inow['longitude']
        timezone = inow['timezone_gmt']
        print("\n\tВведенный IP-адрес {}{}{} ".format(yellow, ip, reset), "\n    Страна - {}{}{}, город - {}{}{}, Провайдер - {}{}{}\n    Широта - {}{}{}, Долгота - {}{}{}, Время GMT - {}{}{}".format(red, country, reset, blue, city, reset, yellow, isp, reset, blue, latitude, reset, blue, longitude, reset, blue, timezone, reset))

    if sys.version_info.major < 3:
        yellow = "\033[33m"
        reset = "\033[0m"
        print("\n\t{}Sorry for the inconvenience, Please run the program in python 3{}\n".format(yellow, reset))
        exit()

import requests


class SocialDeanon:
    def __init__(self):
        yellow = "\033[33m"
        red = "\033[31m"
        reset = "\033[0m"
        self.nickname = input('\n {}[+] Введите никнейм: {}'.format(yellow, reset))
        self.nickname = self.nickname.replace('@', '')

        self.output()

    def availability(self):
        req_list = [
            'https://t.me/',
            'https://www.instagram.com/',
            'https://www.steamcommunity.com/id/',
            'https://github.com/',
            'https://ok.ru/',
            'https://vk.com/',
            'https://soundcloud.com/',
            'https://www.tumblr.com/blog/view/',
            'https://ask.fm/',
            'https://www.deviantart.com/',
            'https://www.flickr.com/',
            'https://ru.linkedin.com/in/',
            'https://myspace.com/',
            'https://www.pinterest.com/',
            'https://www.reddit.com/user/'
        ]

        req_answer = []
        print('\nCollecting data...')
        for req_url in req_list:
            social_req = req_url + self.nickname

            try:
                res = requests.get(social_req)
                if res:
                    print(' ', social_req)
                    req_answer.append(social_req)
                else:
                    print(' ', social_req)
            except:
                print(' ', social_req)

        return req_answer

    def output(self):
        red = "\033[31m"
        reset = "\033[0m"
        if self.nickname != '':
            req_answer = self.availability()

            len_design = 2 + 33 + len(self.nickname)

            a = len(req_answer)
            if a >= 1:
                print(' ' + '=' * len_design)
                print('  [+] Результат:\n')
                for i in req_answer:
                    print('  ' + i)
                print(' ' + '=' * len_design)
                input('{}\n  [+] Нажмите ENTER, чтобы вернуться в главное меню{}'.format(red, reset))
            else:
                print('{}\n Этот ник в социальных сетях не найден!{}'.format(red, reset))
        else:
            print('{}\n [!] ВНИМАНИЕ! Пустой ввод! [!]{}'.format(red, reset))
            input('{}\n [+] Нажмите ENTER, чтобы вернуться в главное меню{}'.format(red, reset))




# Дополнительное задание по модулю Классы и объекты
from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    users = []

    def __init__(self):
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for i in self.users:
            if i.nickname == nickname and i.password == hash(password):
                self.current_user = nickname
                # print(f'Здравствуйте, {nickname}')
            else:
                print(f'Пользователь не найден')

    def log_out(self):
        self.current_user = None

    def register(self, nickname, password, age):
        for i in self.users:
            if i.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        user = User(nickname, hash(password), age)
        self.users.append(user)
        self.current_user = user
        # print(f'Здравствуйте, {nickname}')

    def add(self, *args):
        for i in args:
            if i.title not in self.videos:
                self.videos.append(i)
                # print(self.videos)

    def get_videos(self, find_word):
        find_video = []
        for i in self.videos:
            if find_word.lower() in i.title.lower():
                find_video.append(i.title)
        return find_video

    def watch_video(self, find_title):
        # self.find_title = find_title
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for i in self.videos:
            if find_title == i.title:
                if i.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                else:
                    while i.time_now <= i.duration:
                        print(i.time_now, end=' ')
                        sleep(1)
                        i.time_now += 1
                    print(f'Конец видео')
                    i.time_now = 0


# ur = UrTube()
# ur.register('Петя', '1234', 20)
# ur.register('Вася', 'qwerty', 12)
# ur.register('Петя', 'пароль', 30)
# print()
# ur.log_in('Петя', '1234')
# ur.log_in('Вова', 'abcd')

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
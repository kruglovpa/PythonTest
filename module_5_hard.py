# Дополнительное задание по модулю Классы и объекты
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        user={self.nickname: [self.password, self.age]}


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    users = [{'': ['', 0]}]
    # videos = []

    def __init__(self):
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        self.nickname = nickname
        self.password = hash(password)
        for i in UrTube.users:
            if self.nickname in i:
                if self.password == UrTube.users.values[0](self.nickname):
                    UrTube.current_user = self.nickname
                    print(f'Здравствуйте, {self.nickname}')
                else:
                    print(f'Пароль не верный')
            else:
                print(f'Пользователь не найден')

    def register(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        for i in UrTube.users:
            if self.nickname in i.keys():
                # if self.nickname in i:
                print(f'Пользователь {self.nickname} уже существует')
            else:
                UrTube.users.append({self.nickname: [self.password, self.age]})
                UrTube.current_user = self.nickname
                print(f'Здравствуйте, {self.nickname}')
            break

    def log_out(self):
        UrTube.current_user = None

    def add(self):
        self.title = Video.title
        self.duration = Video.duration
        self.time_now = Video.time_now
        self.adult_mode = Video.adult_mode
        for i in UrTube.videos:
            if self.title not in i:
                UrTube.append([self.title, self.duration, self.time_now, self.adult_mode])

    def get_videos(self, find_word):
        self.finf_word = find_word
        for i in Urube.videos:
            if self.finf_word in i[0]:
                return i[0]

    def watch_video(self, find_title):
        self.finf_title = find_title
        for i in Urube.videos:
            if self.finf_title == i[0]:
                for j in range(i[2], i[1]):
                    return j


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.register('pavel', 'aaa', 40)
print(ur.users)
ur.register('pavel', 'bbb', 30)
print(ur.users)
# ur.log_in('pavel', 'aaa')
# Добавление видео
# ur.add(v1, v2)

# Проверка поиска
# print(ur.get_videos('лучший'))
# print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# ur.watch_video('Для чего девушкам парень программист?')
# ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
# ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
# print(ur.current_user)

# Попытка воспроизведения несуществующего видео
# ur.watch_video('Лучший язык программирования 2024 года!')

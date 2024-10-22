class UrTube:
    users = [{}]

    def __init__(self):
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        self.nickname = nickname
        self.password = password
        if self.nickname in UrTube.users:
            if hash(self.password) == UrTube.users:
                UrTube.current_user = self.nickname

    def log_out(self):
        UrTube.current_user = None

    def register(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        for i in UrTube.users:
            if self.nickname in i.keys():
                print(f'Пользователь {self.nickname} уже существует')
                continue
            else:
                print(self.nickname)
                print(i)
                UrTube.users.append({self.nickname: [hash(self.password), self.age]})
                UrTube.current_user = self.nickname
                print(UrTube.users)
                break


ur = UrTube()
ur.register('Петя', '1234', 20)
ur.register('Вася', 'qwerty', 12)
ur.register('Петя', 'пароль', 30)

# ur.log_in('Вася', 123)

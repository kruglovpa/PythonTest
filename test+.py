class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        # user = {self.nickname: [self.password, self.age]}


class UrTube:
    users = [{'': ['', 0]}]

    def __init__(self):
        self.current_user = None

    def register(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        for i in UrTube.users:
            if self.nickname in i.keys():
                print(f'Пользователь {self.nickname} уже существует')
            else:
                UrTube.users.append({self.nickname: [self.password, self.age]})
                UrTube.current_user = self.nickname
                print(f'Здравствуйте, {self.nickname}')
                print(UrTube.users)
            break


ur = UrTube()
ur.register('Петя', '1234', 20)
ur.register('Вася', 'qwerty', 12)
ur.register('Петя', 'пароль', 30)

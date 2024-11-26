import time

class User:
    def __init__(self, name, mail, phone, password):
        self.name = name
        self.mail = mail
        self.phone = phone
        self.password = password
        self.bd_mail = []
        self.ch_course = ""
        
    def registr(self, mail):
        if mail in self.bd_mail:
            print(f"Пользователь с почтой '{mail}' уже существует")
        else:
            self.bd_mail.append(mail)
            print(f"Новый пользоваетль '{self.name}' зарегестрирован")
        
    def login(self, add_password):
        if self.password == add_password:
            print (f"Пароль '{self.password}' пользователя '{self.name}' верный")
        else:
            print('Пароль неверный')

    def choice_course(self, list_courses):
        while True:
            choice = input(f"\nПользователь {self.name}, введите название выбранного курса:")
            for i in list_courses:
                if choice == i.title:
                    self.ch_course = i.title
                    return print(f"Отлично! Пользователь {self.name}, вы выбрали курс: {i.title}")
            print(f"Пользователь {self.name}, данного курса нет в списке.")

    def pass_tests(self,list_courses):
        print(f"Прохождение пользователем {self.name} тестов по курсу {self.ch_course}:\n")
        for i in list_courses:
            if self.ch_course == i.title:
                for j in i.tests:
                    time.sleep(2)
                    print(f"Прогресс прохождения теста {j}:\n")
                    time.sleep(3)
                    print(f"Тест {j} пройден\n")
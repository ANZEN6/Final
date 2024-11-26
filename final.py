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
                
        
class Course:
    def __init__(self, price, title, term, desc, teacher, subjects, tests):
        self.price = price
        self.title = title
        self.term = term
        self.desc = desc
        self.teacher = teacher
        self.subjects = subjects
        self.tests = tests
    
    def __str__(self):
        return f"Название курса: '{self.title}'\nОписание курса: {self.desc}\nЦена: {self.price} руб.\nКурс обучения: {self.term}\nПреподаватель курса: {self.teacher}"
    
    def add_courses(self,courses,course):
        courses.append(course)
    
    def print_subjects(self,course):
        print(f"Изучаемые модули:")
        for i in course.subjects:
            print(f"- {i}")

    def print_tests(self,course):
        print(f"Тесты:")
        for i in course.tests:
            print(f"- {i}")


course_1 = Course(12000,"JUNIOR-разработчик на Python","1 год","Поможет освоить Python с нуля",
                "Петров Андрей",["Введение в Python","Списки, кортежи и словари","ООП"],["№1","№2","№3"])

course_2 = Course(10000,"JUNIOR-разработчик на JavaScript","2 года","Поможет освоить JavaScript",
                "Фролова Алина",["Основы JavaScript","JavaScript: углубленное изучение","Как написать сайт с помощью JavaScript"],
                  ["№1","№2","№3"])

course_3 = Course(15000,"JUNIOR-разработчик на C++","1 год","Освойте C++ всего за 1 год",
                "Смирнов Сергей",["Программирование на C++","ООП","Стандартные библиотеки C++"],["№1","№2","№3"])

list_courses = []

course_1.add_courses(list_courses,course_1)
course_2.add_courses(list_courses,course_2)
course_3.add_courses(list_courses,course_3)

print(course_1)
course_1.print_subjects(course_1)
course_1.print_tests(course_1)
print("\n<><><><><><><><><><><><><><><><><><><><><>\n")
print(course_2)
course_2.print_subjects(course_2)
course_2.print_tests(course_2)
print("\n<><><><><><><><><><><><><><><><><><><><><>\n")
print(course_3)
course_3.print_subjects(course_3)
course_3.print_tests(course_3)

print("\n<><><><><><><><><><><><><><><><><><><><><>\n")

admin = User("Иванов Иван","ivanov23@mail.ru","89563453289","1234")

admin.registr("ivanov23@mail.ru")
admin.login("1234")

admin.choice_course(list_courses) 

print("\n<><><><><><><><><><><><><><><><><><><><><>\n")

admin.pass_tests(list_courses)

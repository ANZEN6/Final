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
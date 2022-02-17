class Course(object):  # определяем класс курса
    def __init__(self, course):
        self.course = course
        self.students = []

    def __str__(self):
        return str(self.course)

    def enter(self, student):  # метод зачисления на курс
        if student not in self.students:
            student.full_name = student.name + " " + student.surname
            self.students.append(student.full_name)
        else:
            print(student.full_name, 'has been enrolled.')
            pass

    def get_participants(self):  # метод получения списка студентов, зачисленных на курс
        return self.students

    def participants_list(self):  # метод выведения на печать списка студентов, зачисленных на курс
        print('List of' + ' ' + self.course + ' ' + 'Course Participants')
        print(self.get_participants())


class Student(object):  # определяем класс слушателей курсов
    __last_id = 0  # счетчик слушателей курса

    def __init__(self, name, surname):
        Student.__last_id += 1
        self.__id = Student.__last_id
        self.name = name
        self.surname = surname
        self.courses = []
        self.grades = {}

    def full_name(self):
        return self.name + " " + self.surname

    def enroll(self, course):  # Метод поступления на курс
        if course not in self.courses:  # Добавление курса в список
            self.courses.append(course)
        else:
            pass

    def get_courses(self):  # метод получения списка курсов, на которые зачислен слушатель
        return self.courses

    def courses_list(self):  # метод выведения на печать списка курсов, на которые зачислен слушатель
        print('List of Courses for' + ' ' + str(self.full_name))
        print(self.get_courses())


#  создаем курсы
c1 = Course("Python Developer")
c2 = Course("Java Developer")
c3 = Course("Machine Learning")
#  создаем слушателей курсов
st1 = Student('Ivan', 'Petrov')
st2 = Student('Olga', 'Sedova')
st3 = Student('Anton', 'Ivanov')
st4 = Student('Inna', 'Orlova')
#  зачисление на курсы через методы курса
c1.enter(st1)
c2.enter(st2)
c3.enter(st3)
c1.enter(st4)
c1.enter(st3)
#  зачисление на курсы через методы студентов
c1.participants_list()
c2.participants_list()
c3.participants_list()
#  распечатываем списки слушателей каждого курса
st1.enroll(c1)
st2.enroll(c2)
st3.enroll(c3)
st3.enroll(c1)
st4.enroll(c1)
# распечатываем списки курсов, на которые зачислены слушатели
st1.courses_list()
st2.courses_list()
st3.courses_list()
st4.courses_list()

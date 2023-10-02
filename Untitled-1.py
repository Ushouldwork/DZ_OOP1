class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade_l):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.grades_l:
                lecturer.grades_l[course].append(grade_l)
            else:
                lecturer.grades_l[course] = [grade_l]
        else:
            return 'Ошибка'

    def average_rating_s(self):
        total_grades = 0
        total_count = 0
        for course_grades in self.grades.values():
            total_grades += sum(course_grades)
            total_count += len(course_grades)
        if total_count == 0:
            return None  
        return total_grades / total_count

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_rating_s()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершённые курсы: {", ".join(self.finished_courses)}')

    def __lt__(self, other):
        if not isinstance(other, Student) and isinstance(other, Lecturer):
            print('Сравнение невозможно')
        elif (Lecturer.average_rating_l(self, other) < Student.average_rating_s(self, other)):
            return 'Оценка студента, выше оценки лектора'
        elif (Lecturer.average_rating_l(self, other) > Student.average_rating_s(self, other)):
            return 'Оценка студента, ниже оценки лектора'
        else:
            return 'Оценки равны'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades_l = {}

    def average_rating_l(self):
        total_grades = 0
        total_count = 0
        for course_grades in self.grades_l.values():
            total_grades += sum(course_grades)
            total_count += len(course_grades)
        if total_count == 0:
            return None  
        return total_grades / total_count

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating_l()}')


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}')



student_1 = Student('Максим', 'Чернов', 'мужчина')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Олег', 'Иванов', 'мужчина')
student_2.courses_in_progress += ['Python', 'Git']
student_2.finished_courses += ['Введение в программирование']

lecturer_1 = Lecturer('Василий', 'Петров')
lecturer_1.courses_attached += ['Введение в программирование']

lecturer_2 = Lecturer('Иван', 'Голуб')
lecturer_2.courses_attached += ['Введение в программирование']

reviewer_1 = Reviewer('Егор', 'Черных')
reviewer_2 = Reviewer('Ольга', 'Васильева')


reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 10)

reviewer_1.rate_hw(student_1, 'Введение в программирование', 10)
reviewer_2.rate_hw(student_2, 'Введение в программирование', 10)

student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_2, 'Введение в программирование', 10)

student_2.rate_lecturer(lecturer_1, 'Python', 9)
student_2.rate_lecturer(lecturer_2, 'Введение в программирование', 9)

def avg_hw_grade(students, course_name):
    total_grade = 0
    count = 0
    for student in students:
        if course_name in student.grades:
            total_grade += sum(student.grades[course_name])
            count += len(student.grades[course_name])
    return total_grade / count if count > 0 else None

def avg_lecture_grade(lecturers, course_name):
    total_grade = 0
    count = 0
    for lecturer in lecturers:
        if course_name in lecturer.grades_l:
            total_grade += sum(lecturer.grades_l[course_name])
            count += len(lecturer.grades_l[course_name])
    return total_grade / count if count > 0 else None

avg_hw_python = avg_hw_grade([student_1, student_2], 'Python')
print(f'Средняя оценка за домашние задания по Python: {avg_hw_python}')

avg_lecture_python = avg_lecture_grade([lecturer_1, lecturer_2], 'Python')
print(f'Средняя оценка за лекции по Python: {avg_lecture_python}')
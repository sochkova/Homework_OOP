class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def student_rating(self):
        n = 0
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        for k, v in self.grades.items():
            n += 1
            self.student_rating = (sum(self.grades.values())) / n
            res = f'Имя: {self.name}\n' \
                  f'Фамилия: {self.surname}\n' \
                  f'Средняя оценка за домашнее задание:{self.student_rating}\n' \
                  f'Курсы в процессе обучения: {courses_in_progress}\n ' \
                  f'Завершенные курсы: {finished_courses}'
            return res

    def __lt__(self, other_student):
        return self.student_rating < other_student.student_rating

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.grades = {}

    def lecturer_rating(self):
        n = 0
        for k, v in self.grades.items():
            n += 1
            self.lecturer_rating = (sum(self.grades.values())) / n
            res = f'Имя: {self.name}\n' \
                  f'Фамилия: {self.surname}\n' \
                  f'Средняя оценка за домашнее задание: {self.lecturer_rating}\n'
            return res

    def __lt__(self, other_lecturer):
        return self.lecturer_rating < other_lecturer.lecturer_rating

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}'
        return res


# создаем экземпляры класса student:
student1 = Student('Ivan', 'Ivanov', 'Male')
student1.courses_in_progress += ['Git']
student1.finished_courses += ['Python']

student2 = Student('Petr', 'Petrov', 'Male')
student2.courses_in_progress += ['Python']
student2.finished_courses += ['Git']

# создаем список студентов
student_list = [student1, student2]

# создаем экземпляры класса reviewer:
reviewer1 = Reviewer('Oleg', 'Olegov')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Semen', 'Semenov')
reviewer2.courses_attached += ['Git']

# создаем экземпляры класса lecturer:
lecturer1 = Reviewer('Denis', 'Denisov')
lecturer1.courses_attached += ['Python']

lecturer2 = Reviewer('Danil', 'Danilov')
lecturer2.courses_attached += ['Git']

# создаем список лекторов:
lecturer_list = [lecturer1, lecturer2]

# ставим оценки студентам
reviewer1.rate_hw(student2, 'Python', 8)
reviewer1.rate_hw(student2, 'Python', 9)
reviewer1.rate_hw(student2, 'Python', 8)

reviewer2.rate_hw(student1, 'Git', 10)
reviewer2.rate_hw(student1, 'Git', 5)
reviewer2.rate_hw(student1, 'Git', 9)

# ставим оценки лекторам
student1.rate_lecture(lecturer2, 'Python', 7)
student1.rate_lecture(lecturer2, 'Python', 8)
student1.rate_lecture(lecturer2, 'Python', 7)

student2.rate_lecture(lecturer1, 'Git', 6)
student2.rate_lecture(lecturer1, 'Git', 10)
student2.rate_lecture(lecturer1, 'Git', 9)

#функции для подсчета средних оценок лекторов/студентов
def average_rate_student(student_list, course_name):
    sum_all = 0
    count_all = 0
    for student in student_list():
        if [course_name] == student.courses_in_progress:
            sum_all += student.student_rating
            count_all += 1
            average_for_students = sum_all / count_all
            return average_for_students


def average_rate_lecturer(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lecturer in lecturer_list():
        if lecturer.courses_attached == [course_name]:
            sum_all += lecturer.lecturer_rating
            count_all += 1
            average_for_lecturer = sum_all / count_all
            return average_for_lecturer
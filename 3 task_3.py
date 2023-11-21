
from random import *


class Teachers:

    def __init__(self, name_teacher, age, gender, number_students):
        self.age = age
        self.gender = gender
        self.name_teacher = name_teacher
        self.number_students = number_students

    def teach(self, name_material, number):
        numbers = [i for i in range(0, 4)]
        shuffle(numbers)
        for i in numbers[0:number]:
            students[i].take(name_material)
        self.number_students += 1


class Students:

    def __init__(self, name_student, age, gender, knowlenge):
        self.name_student = name_student
        self.knowlenge = knowlenge
        self.age = age
        self.gender = gender

    def take(self, nam):
        self.knowlenge.append(nam)

    def take_knowlenge(self):
        return self.knowlenge

    def lose_knowlenge(self):
        self.knowlenge.remove(choice(self.knowlenge))

    def __len__(self):
        return len(self.knowlenge)


class Data:

    def __init__(self, *args):
        self.args = args

    def take_list(self):
        return [i for i in self.args]

    def __len__(self):
        return len([i for i in self.args])


books_global = Data('Python', 'Version Control Systems', 'Relational Databases', 'NoSQL databases', 'Message Brokers')
books = books_global.take_list()
teach1 = Teachers('Андреева Василиса Викторовна', 26, 'жен', 0)

students = []

students.append(Students('Колосова Алиса Михайловна', 15, 'жен', []))
students.append(Students('Евдокимов Даниил Романович', 14, 'муж', []))
students.append(Students('Воронин Платон Егорович   ', 16, 'муж', []))
students.append(Students('Иванов Степан Ярославович', 14, 'муж', []))


teach1.teach(books[0], randrange(0, 4, 1))
teach1.teach(books[1], randrange(0, 4, 1))
teach1.teach(books[2], randrange(0, 4, 1))
teach1.teach(books[3], randrange(0, 4, 1))
teach1.teach(books[4], randrange(0, 4, 1))

print(students[0].take_knowlenge())
print(students[1].take_knowlenge())
print(students[2].take_knowlenge())
print(students[3].take_knowlenge())
print(len(students[0]))
print(len(books_global))

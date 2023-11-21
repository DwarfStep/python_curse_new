
from random import *


class Teachers:

    def __init__(self, name_teacher, number_students):
        self.name_teacher = name_teacher
        self.number_students = number_students

    def teach(self, name_material, number):
        numbers = [i for i in range(0, 4)]
        shuffle(numbers)
        for i in numbers[0:number]:
            students[i].take(name_material)
        self.number_students += 1


class Students:

    def __init__(self, name_student, knowlenge):
        self.name_student = name_student
        self.knowlenge = knowlenge

    def take(self, nam):
        self.knowlenge.append(nam)

    def take_knowlenge(self):
        return self.knowlenge


class Data:

    def __init__(self, *args):
        self.args = args

    def take_list(self):
        return [i for i in self.args]


books = Data('Python', 'Version Control Systems', 'Relational Databases', 'NoSQL databases', 'Message Brokers').take_list()
teach1 = Teachers('Дмитрий', 0)

students = []

students.append(Students('Анна', []))
students.append(Students('Олег', []))
students.append(Students('Антон', []))
students.append(Students('Андрей', []))

teach1.teach(books[0], randrange(0, 4, 1))
teach1.teach(books[1], randrange(0, 4, 1))
teach1.teach(books[2], randrange(0, 4, 1))
teach1.teach(books[3], randrange(0, 4, 1))
teach1.teach(books[4], randrange(0, 4, 1))

print(students[0].take_knowlenge())
print(students[1].take_knowlenge())
print(students[2].take_knowlenge())
print(students[3].take_knowlenge())

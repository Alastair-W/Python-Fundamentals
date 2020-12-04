class Person:
    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number


class Student(Person):
    # UNDERGRADUATE, POSTGRADUATE = range(2)
    def __init__(self, student_type, *args, **kwargs):
        self.student_type = student_type
        self.classes = []
        # super(Student, self).__init__(*args, **kwargs)

    def enrol(self, course):
        self.classes.append(course)



jane = Student("Jane", "Smith", "SMTJNX045")
print(jane.name)
# jane.enrol(a_postgrad_course)

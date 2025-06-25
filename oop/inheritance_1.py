class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def show_info(self):
        print("Name:", self.name)
        print("ID:", self.id)

class Student(Person):
    def __init__(self, name, id, sem):
        super().__init__(name, id)
        self.sem = sem

    def show_info(self):
        super().show_info()
        print("Semester:", self.sem)

s1 = Student("Bikesh", 7, "Second")
s1.show_info()

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

class graduate(Student):
    def __init__(self, name, id, sem, gpa):
        super().__init__(name, id, sem)
        self.gpa=gpa
    def show_info(self):
        super().show_info()
        print("Gpa:",self.gpa)
gs1=graduate("Bikesh",7,"Second",3.7) 
gs1.show_info()       

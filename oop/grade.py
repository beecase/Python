class Student:
    def __init__(self):
        self.name = None
        self.roll = None
        self.gpa = None

    def getInput(self):
        self.name = input("What is your name?")
        self.roll = int(input("What is your roll?"))
        self.gpa = float(input("What is your GPA?"))
        while self.gpa > 4.0:
            print("INVALID")
            self.gpa = float(input("What is your GPA?"))
        return self.roll, self.name, self.gpa

    def showInfo(self):
        print("Name: " + self.name)
        print(f"Roll: {self.roll}")
        print(f"GPA: {self.gpa}")

    def checkGrade(self):
        if self.gpa:
            if self.gpa == 4:
                print("Your grade is A+")
            else:
                print("Your grade is not A+")

stud = Student()
stud.getInput()
stud.showInfo()
stud.checkGrade()


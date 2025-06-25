"""class person:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
class student(person):
    def __init__(self, name, roll,sem):
        super().__init__(name, roll)
        self.sem=sem
    def show(self):
        print(self.name)
        print(self.roll)
        print(self.sem) 
s=student("ram",2,2)               
s.show()"""
def summ(*args):
    return sum(args)
a=[1,2,3]
print(summ(*a))
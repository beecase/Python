class rectangle:

    def __init__(self,l,b):
        self.length=l
        self.breadth=b

    def area(self):
        return self.length*self.breadth
    
    def perimeter(self):
        return 2*( self.length+self.breadth)
rect1=rectangle(9,3)
print(f"Area having length {rect1.length} and breadth {rect1.breadth} is:{rect1.area()}")
print(f"Perimeter having length {rect1.length} and breadth {rect1.breadth} is:{rect1.perimeter()}")
rect2=rectangle(10,5)
print(f"Area having length {rect2.length} and breadth {rect2.breadth} is:{rect2.area()}")
print(f"Perimeter having length {rect2.length} and breadth {rect2.breadth} is:{rect2.perimeter()}")


       
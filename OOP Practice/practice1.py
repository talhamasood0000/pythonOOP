#Create a Cricle class and intialize it with radius. Make two methods getArea and getCircumference inside this class.

class Circle:
    def __init__(self, radius:float):
        self.radius=radius
    
    def getArea(self):
        area=0
        float(area)
        area=3.14*self.radius*self.radius
        return area
        
    def getCircumference(self):
        circum=0
        float(circum)
        circum=2*3.1416*self.radius
        return circum

sm_circle=Circle(3)
print(sm_circle.getArea())
print(sm_circle.getCircumference())
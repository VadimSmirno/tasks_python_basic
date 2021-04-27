import  math

class Сircle:

    def __init__(self,x,y,radius):
        self.x = x
        self.y = y
        self.radius = int(radius)


    def area(self):
        area = math.pi*self.radius**2
        return area

    def perimeter(self):
        return 2*math.pi*self.radius

    def big_circle(self):
        coefficient = int(input('Во сколько раз увеличить круг'))
        return  math.pi*self.radius**2*coefficient

    def crossing(self):
       d = math.sqrt((сircle1.x - сircle2.x)**2 + (сircle1.y - сircle2.y))
       if d > (сircle1.radius + сircle2) or 0 < d < math.fabs(сircle1.radius - сircle1.radius):
           print ('общих точек нет')
       elif d == (сircle1.radius + сircle2) or   d == math.fabs(сircle1.radius - сircle1.radius):
           print ('Есть одна общая точка')
       else:
           print ('Есть две общие точки')



сircle1 = Сircle(1,5,2)
сircle2 = Сircle(2,4,6)
print(сircle1.perimeter())
сircle1.crossing()
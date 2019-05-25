class Square(object):

    def __init__(self,length):
        self.length = 10
    def area (self):
        return self.length**2
    def diag (self):
        return self.length

q = Square(10)
print q.area()
print q.diag()

class Vehicle(object):

    def __init__(self,id,speed):
        self.id = id
        self.speed = speed
    def __str__(self):
        return "Vehicle id: ",self.id,"speed: ",self.speed

class Bus(Vehicle):

    def __init__(self,id,speed,pa=0):
        Vehicle.__init__(self,id,speed)
        self.passengers = pa
        self.id = id
        self.speed = speed
    def __str__(self):
        return "Bus id: %d speed %d  passengers %d"%( self.id, self.speed,self.passengers)

b = Bus(3,45)
print b

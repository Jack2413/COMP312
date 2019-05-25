from SimPy.Simulation  import *
from random import randint
#import simpy

#kathy(a)
class Customer(Process):

    def visitA (self,timeInMuseum):
        print now(),self.name,"This is new"
        yield hold, self,timeInMuseum
        print now(),self.name,"Nice Place!"

    def visitB (self,displayTime):

        print self.name,"Look!, number 0",now()
        yield hold, self,displayTime[0]
        print self.name,"mm",now()
        print self.name,"Look!, number 1",now()
        yield hold, self,displayTime[1]
        print self.name,"mm",now()

    def visitC (self,displayTime):
        
        print self.name,"Look!, number 0",now()
        yield hold, self,displayTime[0]
        
        if(random.random()<=0.4):
            print self.name,"Look!, number 2",now()
            yield hold, self,displayTime[1]
            
        else:
            print self.name,"Look!, number 2",now()
            yield hold, self,displayTime[2]
            

    def visitD (self,displayTime):
        print self.name,"Look!, number 0",now()
        yield hold, self,displayTime
        print self.name,"mm",now()
       
        while(random.random()<=0.4):
            yield hold, self,displayTime
            print self.name,"mm",now()
      

            
initialize()
c = Customer(name="Kathy")
activate(c,c.visitA(10),at=0.0)
simulate(until=20.0)


#0 Kathy This is new
#10 Kathy Nice Place!

#kathy(b)
initialize()
c = Customer(name="Kathy")
activate(c,c.visitB([4.5,5.5]),at=0.0)
simulate(until=20.0)

#kathy Look!, number 0 0
#Kathy mm 4.5
#Kathy Look!, number 1 4.5
#Kathy mm 10.0


#kathy(c)

initialize()
random.seed(99999)
c = Customer(name="Kathy")
activate(c,c.visitC([4.5, 5.5, 7.5]),at=0.0)
simulate(until=20.0)

#Kathy Look!, number 0 0
#Kathy Look!, number 2 4.5

#kathy(d)
initialize()
random.seed(99999)
c = Customer(name="Kathy")
activate(c,c.visitD(4.5),at=0.0)
simulate(until=100.0)

#Kathy Look!, number 0 0
#Kathy mm 4.5
#Kathy mm 9.0
#Kathy mm 13.5


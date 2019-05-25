import random
def trials(n,t):
    random.seed(123)
    double6 = 0
   
    for i in range(n):
        dice1List = []
        dice2List = []
        for i in range(t):
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            dice1List.append(dice1)
            dice2List.append(dice2)
            if dice1==6 and dice2==6:
                double6+=1
                #print dice1List,"\n", dice2List
                break       
    return double6

n=100000 #trials
t=24 #throws
d6 = trials(n,t)
p= (float) (d6)/n
print "double-6: ",d6
print "The possibility of get at least one double 6 on on ",t ," throws on",n,"trials is: ",p
# the answer is less than 1/2

while (p<0.5):
    t+=1
    d6 = trials(n,t)
    p= (float) (d6)/n
    print "The possibility of get at least one double 6 on on ",t ," throws on",n,"trials is: ",p
print t, "throws could be just greater than 1/2"

import random
def tablelookup(y,p):
    #"""Sample from y[i] with probabilities p[i]"""
    u = random.random()
    sumP = 0.0
    for i in range(len(p)):
        sumP += p[i]
        if u < sumP:
            dict1 = {'chosen':y[i],'step':i+1}
            return dict1
random.seed(123)
y = [0,1,2,3,4,5]
p = [1.0/1024, 15.0/1024, 90.0/1024, 270.0/1024, 405.0/1024, 243.0/1024]
m = 1000000
valuetotal = 0.0
for k in range(m):
    d = tablelookup(y,p)
    valuetotal += d['chosen']
print valuetotal/m

#b)
#i)
y = [0,1,2,3,4,5]
stepTotal = 0.0
for k in range(m):
    d = tablelookup(y,p)
    step = d['step']
    stepTotal += step
print "the average number of steps over ",m," trials: ",stepTotal/m
#ii)
stepTotal = 0.0
y = [5,4,3,2,1,0]
p = [243.0/1024, 405.0/1024, 270.0/1024, 90.0/1024, 15.0/1024, 1.0/1024]
for k in range(m):
    d = tablelookup(y,p)
    step = d['step']
    stepTotal += step
print "the average number of steps over ",m," trials: ",stepTotal/m
#iii)
stepTotal = 0.0
y = [5,4,3,2,1,0]
p = [405.0/1024, 270.0/1024, 243.0/1024, 90.0/1024, 15.0/1024, 1.0/1024]
for k in range(m):
    d = tablelookup(y,p)
    step = d['step']
    stepTotal += step
print "the average number of steps over ",m," trials: ",stepTotal/m


   

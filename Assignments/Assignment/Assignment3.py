import math
import random
 


class Ellipse(object):

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def area(self):
        area = math.pi*self.a*self.b
        print "area: ",area
        return area

    def eccentricty(self):
        eccentricity = (1-(self.b/self.a)**2)**0.5
        print "eccentricity: ",eccentricity
        return eccentricity

x=Ellipse(10.0,5.0)
x.area()
x.eccentricty()

#area:  157.079632679
#eccentricity:  0.866025403784

#a
def chisquarevariate(k):   
    ans=0
    for i in range (1,k+1):
        x = random.normalvariate(0,1)
        ans+=x**2
    return ans
#b
def count ():
    
    k=[1,2,3,4,5,6,7,8,9]
    sumlist = [0,0,0,0,0,0,0,0,0]
    exp = [0,0,0,0,0,0,0,0,0]
    var = [0,0,0,0,0,0,0,0,0]
  
    
    for j in range (9):
        list1=[]
        sumV=0
        for i in range(10000):
             list1.append(chisquarevariate(k[j]))
             sumlist[j] += list1[i]
             sumV += (list1[i]**2)

        exp[j] = sumlist[j]/10000
        var[j] = sumV/10000-exp[j]**2

    print "Exp: ",exp
    print "Var: ",var
#Exp:  [0.9859589433220745, 1.9661749109569646, 3.0309128243308594, 3.9915319982901223, 5.011899315651698, 6.044197451478812, 7.025488286176544, 7.9621049928653855, 9.042364970199703]
#Var:  [1.9393569513355953, 3.8551185446990597, 6.241066543206562, 8.038005739815775, 10.200407027372933, 12.284337274532056, 14.237621701800684, 15.828959166162818, 18.157492449741454]

count()

def chisquarevariate1(k):   
    ans=0
    for i in range (1,k+1):
        x = random.normalvariate(0,1)
        ans+=x**2
    return ans

#c)

def count1 ():
    
    k=[1,2,3,4,5,6,7,8,9]
    sumlist = [0,0,0,0,0,0,0,0,0]
    exp = [0,0,0,0,0,0,0,0,0]
    var = [0,0,0,0,0,0,0,0,0]
    
    
    for j in range (9):
        list1=[]
        sumV=0
        for i in range(5000):
             list1.append(chisquarevariate(k[j]))
             sumlist[j] += list1[i]
             sumV += (list1[i]**2)

        exp[j] = sumlist[j]/5000
        var[j] = sumV/5000-exp[j]**2

    exp1 = [0,0,0,0,0,0,0,0,0]
    var1 = [0,0,0,0,0,0,0,0,0]
    exp2 = [0,0,0,0,0,0,0,0,0]
    var2 = [0,0,0,0,0,0,0,0,0]
    

    for z in range (9):
        CI = 1.96*(var[z]**0.5)
        exp1[z]=exp[z]+CI
        exp2[z]=exp[z]-CI
        var1[z]=var[z]+CI
        var2[z]=var[z]-CI


    print "Exp1: ",exp1
    print "Exp2: ",exp2
    print "Var1: ",var1
    print "Var2: ",var2
    print CI
count1()


#d)
# to campare with both result arts b and c, they both very close to the exacte valus of E(X) and Var(X) i find
# in witch as k and 2k. especially in C the E(x) value and Var value are in range of 95% confidence interval.




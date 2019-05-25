# -*- coding: utf-8 -*-
# Part 1 — Python
# 1 Write fragments of Python code for the following:
# a You have a dictionary, D={'a':100}. Add a new component with key 'b' and value 200

D={'a':100}
D['b']=200
print D

# b You have a dictionary D={'b':200, 'a':100}. Remove the component with value 200.

D={'b':200, 'a':100}
for key in D.keys():
    if D[key]==200:
        del D[key]
print D
    
# c You have a list, L=[100]. Add a new component with value 200.

L = [100]
L.append(200)
print L

# d You have a list, L=[100,200]. Delete the component with value 200.
L.remove(200)
print L

# e You have a tuple, T=(100,200,300). Unpack T into three separate components, a, b,
#and c

T = (100,200,300)
a=T[0]
b=T[1] 
c=T[2]

#2 Suppose the radius of a circle, r, is a random number (it has a uniform distribution in the
#interval from 0 to 1), and consider the area of the circle, i.e., A = πr2
#.
#(a) 
import random
from math import pi
random.seed(123)
n=10
L=[]
for k in range(n):
    r =random.random()
    A=pi*r**2
    t = (A,r)
    L.append(t)
print L

#b)
total_A=0
total_R=0
for k in range(n):
    total_A+=L[k][0]
    total_R+=L[k][1]
mean_A=total_A/n
mean_R=total_R/n

print "mean_A: ",mean_A,"mean_R: ",mean_R

#c)

random.seed(123)
n=1000000
L=[]
for k in range(n):
    r =random.random()
    A=pi*r**2
    t = (A,r)
    L.append(t)

total_A=0
total_R=0
for k in range(n):
    total_A+=L[k][0]
    total_R+=L[k][1]
mean_A=total_A/n
mean_R=total_R/n

compare_A = pi*mean_R**2
print "compare: ", compare_A, "mean_A ",mean_A




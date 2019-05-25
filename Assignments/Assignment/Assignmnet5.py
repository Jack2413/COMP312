"""(q3.py) M/M/c queueing system with monitor
   and multiple replications"""
#1

from SimPy.Simulation import *
import random
import numpy
import math

## Useful extras ----------
def conf(L):
    """confidence interval"""
    lower = numpy.mean(L) - 1.96*numpy.std(L)/math.sqrt(len(L))
    upper = numpy.mean(L) + 1.96*numpy.std(L)/math.sqrt(len(L))
    return (lower,upper)

## Model ----------
class Source(Process):
    """generate random arrivals"""
    def run(self, N, lamb, mu):
        for i in range(N):
            a = Arrival(str(i))
            activate(a, a.run(mu))
            t = random.expovariate(lamb)
            yield hold, self, t

class Arrival(Process):
    """an arrival"""
    def run(self, mu):
        arrivetime = now()
        if(Arrival.n<K):
            G.m[Arrival.n].observe(1)
            for i in range(K):
                if i != Arrival.n:
                    G.list[i].observe(0)
                    
        yield request, self, G.server
        t = random.expovariate(mu)
        yield hold, self, t
        yield release, self, G.server
        Arrival.n -= 1
        if(Arrival.n<K):
            G.list[Arrival.n].observe(1)
            for i in range(K):
                if i != Arrival.n:
                     G.list[i].observe(0)

        delay = now()-arrivetime
        G.delaymon.observe(delay)



class G:
    server = 'dummy'
    delaymon = 'Monitor'
    list1=[]

def model(c, N, lamb, mu, maxtime, rvseed):
    # setup
    initialize()
    random.seed(rvseed)
    G.server = Resource(c,monitored=True)
    G.delaymon = Monitor()
     for i in range(K):
        G.list1.append(Monitor())
   
    # simulate
    s = Source('Source')
    activate(s, s.run(N, lamb, mu))
    simulate(until=maxtime)
   
    # gather performance measures
    W = G.delaymon.mean()
    WQ=G.server.waitMon.timeAverage()
    LQ= WQ*lamb
    MK=[]

    return(W,WQ,LQ,MK)

## Experiment ----------
K=10
allW= []
allWQ=[]
allLQ=[]
allMK=[]
for k in range(50):
   seed = 123*k
   result = model(c=1, N=10000, lamb=0.96, mu=1.00,
                  maxtime=2000000, rvseed=seed)
   allW.append(result[0])
   allWQ.append(result[1])
   allLQ.append(result[2])
   allMK.append(result[3])
print allW
print ""
print "all MK: ", allMK[0]
print "Estimate of W:",numpy.mean(allW)
print "Conf int of W:",conf(allW)
print "Estimate of WQ:",numpy.mean(allWQ)
print "Conf int of WQ:",conf(allWQ)
print "Estimate of LQ:",numpy.mean(allLQ)
print "Conf int of LQ:",conf(allLQ)

#2
import numpy as np
import matplotlib.pyplot as pl
x=np.linspace(-4,4,1000)
y=np.piecewise(x,[x!=0,x==0],[np.sin(np.pi*x)/(np.pi*x),1])

pl.clf()
pl.plot(x,y,'r-')
pl.title("f(x) = {(sinpi/pix,  x != 0) or (1, x=0)} ",fontsize=16)
pl.xlabel("x",fontsize=16)
pl.ylabel("y",fontsize=16)
pl.axis("tight")
pl.savefig("figure.png")
pl.show()




#1.
from SimPy.Simulation import *
import random
import numpy
import math

## Useful extras ----------
def tablelookup(P):
    """Sample from i=0..n-1 with probabilities P[i]"""
    u = random.random()
    sumP = 0.0
    for i in range(len(P)):
        sumP += P[i]
        if u < sumP:
            return i

def conf(L):
    """confidence interval"""
    lower = numpy.mean(L) - 1.96*numpy.std(L)/math.sqrt(len(L))
    upper = numpy.mean(L) + 1.96*numpy.std(L)/math.sqrt(len(L))
    return (lower,upper)

## Model ----------
class Source(Process):
    """generate random arrivals"""
    def run(self, N, lamb):
        for i in range(N):
            a = Arrival(str(i))
            activate(a, a.run())
            t = random.expovariate(lamb)
            yield hold, self, t

class Arrival(Process):
    """an arrival"""
    n = 0  # class variable (number in system)

    def run(self):
        Arrival.n += 1   # number in system
        arrivetime = now()
        G.numbermon.observe(Arrival.n)

	current = G.startnode
	while (current <> G.outnode):
            yield request,self,G.server[current]
            t = random.expovariate(G.mu[current])
            yield hold,self,t
            yield release,self,G.server[current]
            current = tablelookup(G.transition[current])

        Arrival.n -= 1
        G.numbermon.observe(Arrival.n)
        delay = now()-arrivetime
        G.delaymon.observe(delay)

class G:
    server = 'dummy'
    delaymon = 'Monitor'
    numbermon = 'Monitor'
    startnode = 0
    outnode = 3
    mu = [1/1.0, 1/1.0, 1/1.0]
    transition = [[0.0, 0.1, 0.9, 0.0],
                  [0.2, 0.0, 0.5, 0.3],
                  [0.0, 0.1, 0.0, 0.9]]

def model(N, lamb, maxtime, rvseed):
    # setup
    initialize()
    random.seed(rvseed)
    G.server = [Resource(2),Resource(2),Resource(2)]
    G.delaymon = Monitor()
    G.numbermon = Monitor()
   
    # simulate
    s = Source('Source')
    activate(s, s.run(N, lamb))
    simulate(until=maxtime)

    # gather performance measures
    W = G.delaymon.mean()
    L = G.numbermon.timeAverage()
    return(W,L)

## Experiment ----------------

allW = []
allL = []
allLambdaEffective = []
for k in range(50):
    seed = 123*k
    result = model(N=10000, lamb=1.6,
                  maxtime=2000000, rvseed=seed)
    allW.append(result[0])
    allL.append(result[1])
    allLambdaEffective.append(result[1]/result[0])

print "Estimate of W:",numpy.mean(allW)
print "Conf int of W:",conf(allW)
print "Estimate of L:",numpy.mean(allL)
print "Conf int of L:",conf(allL)
print "Estimate of LambdaEffective:",numpy.mean(allLambdaEffective)
print "Conf int of LambdaEffective:",conf(allLambdaEffective)

#OUTPUT:
#Estimate of W: 6.87174636875
#Conf int of W: (6.732020810873318, 7.01147192661968)
#Estimate of L: 10.9660720227
#Conf int of L: (10.724309048752211, 11.207834996743063)
#Estimate of LambdaEffective: 1.59515494618
#Conf int of LambdaEffective: (1.5911249415081623, 1.5991849508609284)

#2.
from SimPy.Simulation import *
import random
import numpy
import math

## Useful extras ----------
def tablelookup(P):
    """Sample from i=0..n-1 with probabilities P[i]"""
    u = random.random()
    sumP = 0.0
    for i in range(len(P)):
        sumP += P[i]
        if u < sumP:
            return i

def conf(L):
    """confidence interval"""
    lower = numpy.mean(L) - 1.96*numpy.std(L)/math.sqrt(len(L))
    upper = numpy.mean(L) + 1.96*numpy.std(L)/math.sqrt(len(L))
    return (lower,upper)

## Model ----------
class Job(Process):
    """a job"""
    def run(self,N):
        starttime = now()
        current = G.startnode
        for i in range(N):
            yield request,self,G.server[current]
            t = random.expovariate(G.mu[current])
            yield hold,self,t
            yield release,self,G.server[current]
            delay = now()- starttime
            G.delaymon[current].observe(delay)
            current = tablelookup(G.transition[current])
            starttime = now()

class G:
    p=0.5
    server = 'dummy'
    delaymon = 'Monitor'
    startnode = 0
    mu = [1.0/20.0, 1/10.0, 1/30.0]
    transition = [[0.0, p, 1-p],
                  [1.0, 0.0, 0.0],
                  [0.0, 1.0, 0.0]]

def model(N, maxtime, rvseed):
    # setup
    initialize()
    random.seed(rvseed)
    G.server = [Resource(1,monitored=True),
                Resource(1,monitored=True),
                Resource(1,monitored=True)]
                              
    G.delaymon = [Monitor(),Monitor(),Monitor()]
       
    # simulate
    for i in range(5):
        j = Job(str(i))
        activate(j, j.run(N))
    simulate(until=maxtime)

    # gather performance measures
    W = []
    for i in range(len(G.delaymon)):
        W.append(G.delaymon[i].mean())                        
    Lnode = []
    for i in range(len(G.server)):
        h = G.server[i].waitMon.timeAverage() + G.server[i].actMon.timeAverage()
        Lnode.append(h)
    return(W,Lnode)

## Experiment ----------------

allW = [[],[],[]]
allLnode = [[],[],[]]
for k in range(50):
    seed = 123*k
    result = model(N=10000, maxtime=2000000, rvseed=seed)
    for i in range(3):
       allW[i].append(result[0][i])
    for i in range(3):
       allLnode[i].append(result[1][i])

for i in range(3):
    print "Estimate of W[",str(i),"]:",numpy.mean(allW[i])
    print "Conf int of W[",str(i),"]:",conf(allW[i])
for i in range(3):
    print "Estimate of Lnode[",str(i),"]:",numpy.mean(allLnode[i])
    print "Conf int of Lnode[",str(i),"]:",conf(allLnode[i])


#OUTPUT:
#Estimate of W[ 0 ]: 62.0791835885
#Conf int of W[ 0 ]: (61.87476153298064, 62.28360564408635)
#Estimate of W[ 1 ]: 16.432897066
#Conf int of W[ 1 ]: (16.383451993551112, 16.48234213851739)
#Estimate of W[ 2 ]: 66.9006773829
#Conf int of W[ 2 ]: (66.51026511197341, 67.29108965392598)
#Estimate of Lnode[ 0 ]: 2.76456593542
#Conf int of Lnode[ 0 ]: (2.7558963643151984, 2.7732355065151086)
#Estimate of Lnode[ 1 ]: 0.731710499805
#Conf int of Lnode[ 1 ]: (0.7291628359030954, 0.7342581637073476)
#Estimate of Lnode[ 2 ]: 1.48853745204
#Conf int of Lnode[ 2 ]: (1.4791613739513103, 1.4979135301278395)

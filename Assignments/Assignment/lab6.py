from SimPy.Simulation import *
import random
import numpy
import math

## Useful extras ----------
def conf(x):
    """95% confidence interval"""
    lower = numpy.mean(x) - 1.96*numpy.std(x)/math.sqrt(len(x))
    upper = numpy.mean(x) + 1.96*numpy.std(x)/math.sqrt(len(x))
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
    n = 0  # class variable (number in system)

    def run(self, mu):
        Arrival.n += 1   # number in system
        arrivetime = now()
        G.numbermon.observe(Arrival.n)

        ### Observe j customers in system
        for j in range(K):
            if (j != Arrival.n):
                G.m[j].observe(0)
        if (Arrival.n < K):
            G.m[Arrival.n].observe(1)
         
        yield request, self, G.server

        ### --- Could put a monitor on WQ here ---
	
        t = random.expovariate(mu)
        yield hold, self, t
        
        yield release, self, G.server
        Arrival.n -= 1
        G.numbermon.observe(Arrival.n)
        delay = now()-arrivetime
        G.delaymon.observe(delay)

        

        ### Observe j customers in system
        for j in range(K):
            if (j != Arrival.n):
                G.m[j].observe(0)
        if (Arrival.n < K):
            G.m[Arrival.n].observe(1)

class G:
    server = 'dummy'
    delaymon = 'Monitor'
    numbermon = 'Monitor'
    m = 'list of Monitors'
   
def model(s, N, lamb, mu, maxtime, rvseed):
    # setup
    initialize()
    random.seed(rvseed)
    G.server = Resource(s,monitored=True)
    G.delaymon = Monitor()
    G.numbermon = Monitor()

    ### List of monitors
    G.m = []
    for i in range(K):
        G.m.append(Monitor())

    # simulate
    s = Source('Source')
    activate(s, s.run(N, lamb, mu))
    simulate(until=maxtime)

    # gather performance measures
    W = G.delaymon.mean()
    L = G.numbermon.timeAverage()
    P = []
    for j in range(K):
        P.append(G.m[j].timeAverage())
    LQ = G.server.waitMon.timeAverage()
    lambeff = L/W
    WQ = LQ/lambeff

    return(WQ,LQ,P)
  

## Experiment ----------------
K = 10
allWQ = []
allLQ = []
allP = []
for j in range(K):
    allP.append([])
for k in range(50):
    seed = 123*k
    result = model(s=1, N=10000, lamb=2.0, mu=3.0, maxtime=2000000, rvseed=seed)
    allWQ.append(result[0])
    allLQ.append(result[1])
    tempP = result[2]
    for j in range(K):
        allP[j].append(tempP[j])


a = numpy.mean(allWQ)
(b,c) = conf(allWQ)
rho = 2.0/3.0
LQ = (rho**2)/(1-rho)
WQ = LQ/2.0
print "WQ: expect=%6.4f   point=%6.4f   ci=(%6.4f,%6.4f)"%(WQ,a,b,c)

a = numpy.mean(allLQ)
(b,c) = conf(allLQ)
print "LQ: expect=%6.4f   point=%6.4f   ci=(%6.4f,%6.4f)"%(LQ,a,b,c)

p = []
for j in range(K):
    p.append(math.pow(rho,j)*(1-rho))

for j in range(K):
    a = numpy.mean(allP[j])
    (b,c) = conf(allP[j])
    print "pi[%1d]:  expect=%6.4f   point=%6.4f   ci=(%6.4f,%6.4f)"%(j,p[j],a,b,c)

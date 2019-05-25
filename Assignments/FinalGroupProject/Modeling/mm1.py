"""M/M/1 queueing system"""

from SimPy.Simulation import *
import random
import math
import numpy



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
    ## 'n' customers
    n = 0
    
    def run(self, mu):
        # Event: arrival
        Arrival.n += 1   # number in system
        arrivetime = now()
        G.numbermon.observe(Arrival.n)
        if (Arrival.n>0):
            G.busymon.observe(1)
        else:
            G.busymon.observe(0)
            
        yield request, self, G.server
        # ... waiting in queue for server to be empty (delay) ...
        waitTime = now()-arrivetime
        G.waitmon.observe(waitTime)
        # Event: service begins
        t = random.expovariate(mu)
      
        yield hold, self, t
        # ... now being served (activity) ...
      
        # Event: service ends
        yield release, self, G.server # let go of server (takes no simulation time)
        Arrival.n -= 1
        G.numbermon.observe(Arrival.n)
        if (Arrival.n>0):
            G.busymon.observe(1)
        else:
            G.busymon.observe(0)
            
        delay = now()-arrivetime
        G.delaymon.observe(delay)
        G.servicemon.observe(delay-waitTime)


class G:
    server = 'dummy'
    delaymon = 'Monitor'
    numbermon = 'Monitor'
    busymon = 'Monitor'
    waitmon ='Monitor'
    servicemon = 'Monitor'
   


def model(c, N, lamb, mu, maxtime, rvseed):
    # setup
    initialize()
    random.seed(rvseed)
    G.server = Resource(c,monitored=True)
    G.delaymon = Monitor()
    G.numbermon = Monitor()
    G.busymon = Monitor()
    G.waitmon = Monitor()
    G.servicemon = Monitor()
    
    
    # simulation run
    s = Source('Source')
    activate(s, s.run(N, lamb, mu))
    simulate(until=maxtime)

    # gather performance measures
    W = G.delaymon.mean()
    L = G.numbermon.timeAverage()
    LQ = G.server.waitMon.timeAverage()
    LS = G.server.actMon.timeAverage()
    B = G.busymon.timeAverage()
    WQ = G.waitmon.mean()
    WS = G.servicemon.mean()
    return(W,L,B,WQ,WS,LQ,LS)

## Experiment ----------
allW = []
allL = []
allB = []
allWS= []
allWQ= []
allLS= []
allLQ= []
allLambdaEffective = []
for k in range(50):
    seed = 123*k
    result = model(c=1, N=10000, lamb=1/109.225811, mu=1/35.458,
                  maxtime=2000000, rvseed=seed)
    allW.append(result[0])
    allL.append(result[1])
    allB.append(result[2])
    allWQ.append(result[3])
    allWS.append(result[4])
    allLQ.append(result[5])
    allLS.append(result[6])
    allLambdaEffective.append(result[1]/result[0])

print ""
print "Estimate of W:",numpy.mean(allW)
print "Conf int of W:",conf(allW)
print "Estimate of WQ:",numpy.mean(allWQ)
print "Conf int of WQ:",conf(allWQ)
print "Estimate of WS:",numpy.mean(allWS)
print "Conf int of WS:",conf(allWS)
print "Estimate of L:",numpy.mean(allL)
print "Conf int of L:",conf(allL)
print "Estimate of LQ:",numpy.mean(allLQ)
print "Conf int of LQ:",conf(allLQ)
print "Estimate of LS:",numpy.mean(allLS)
print "Conf int of LS:",conf(allLS)
print "Estimate of B:",numpy.mean(allB)
print "Conf int of B:",conf(allB)


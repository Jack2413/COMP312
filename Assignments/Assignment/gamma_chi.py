import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
import math

""" data analysis with chi-square goodness of fit"""

def obs_cts(n, data):
    """ given: the data and number of bins
        returns: the observed values and the bin edges as lists"""
    events, edges = np.histogram(data, n)
    return events.tolist() , edges.tolist()

def exp_cts(n, data):
    """ given: the data and number of bins
        returns: the expected values and prob over each of the bins with
        the necessary modification of the first and last bins"""
    L=[]
    P_bins =[]
    for x in obs_cts(n,data)[1]:
        L.append(rv.cdf(x))
    P_bins.append(L[1])    
    for i in range(1,len(L)-2):
        P_bins.append(L[i+1]-L[i])    
    P_bins.append(1-L[-2])
    exp_cnt = [x * len(data) for x in P_bins]
    return exp_cnt, P_bins

def ind_bins_to_reduce(f_exp):
    """ given: a list
        returns: the indexes of the elements < 5"""
    NC_to_red =[index for index,value in enumerate(f_exp) if value < 5]
    return NC_to_red

def one_reduce(f_exp, f_obs, f_edge):
    """ given: lists of exp, obs, edges
        returns: new lists with one reduced bin with value < 5 """
    BTR = ind_bins_to_reduce(f_exp)
  
    if (len(BTR)>1 or (len(BTR)==1 and BTR[0]!=0)):
        f_exp[BTR[-1]-1] = f_exp[BTR[-1]-1]+f_exp[BTR[-1]]
        f_obs[BTR[-1]-1] = f_obs[BTR[-1]-1]+f_obs[BTR[-1]]
        del(f_edge[BTR[-1]])
        del(f_obs[BTR[-1]])
        del(f_exp[BTR[-1]])
    else:
        if BTR[0]==0:
            f_exp[1]= f_exp[1]+f_exp[0]
            f_obs[1]= f_obs[1]+f_obs[0]
            del(f_edge[1])
            del(f_obs[0])
            del(f_exp[0])

    f_expN = f_exp
    f_obsN = f_obs
    f_edgeN = f_edge
    BTRN = ind_bins_to_reduce(f_expN)
    return f_expN, f_obsN, f_edgeN, BTRN

def all_reduce(f_expF, f_obsF, f_edgeF, BTRF):
    """ finalizes the bin reduction """
    while BTRF !=[]:
        u = one_reduce(f_expF, f_obsF, f_edgeF)
        f_expF = u[0]
        f_obsF = u[1]
        f_edgeF = u[2]
        BTRF = u[3]
    return f_expF, f_obsF, f_edgeF, BTRF


def model(data, n, dof):
        """ given data, the number of bins (n) and the number of estimated parameters (dof)
        produces the value of the chi-squate test statistics and the p-value"""

        ## final expected count and final observed count after amalgamating bins
        exp, obs = all_reduce(exp_cts(n, data)[0],obs_cts(n, data)[0],
                obs_cts(n, data)[1], ind_bins_to_reduce(exp_cts(n, data)[0]))[0:2] 

        # build in chi-gof test, the last argument is the adjustment to the dof
        result = ss.chisquare( np.asarray(obs), np.asarray(exp), dof) 
        return result 

def loadData(fname):
    with open(fname,'r') as fp:
        temp_data=[]
        
        for line in fp:
            line.strip("\n")
            temp_data.append(float(line))
        return temp_data
if __name__ == "__main__":

    ## experiment data --------------------------------------------------------------

    #generate data or read your raw data - for this example the data are iid gamma
    np.random.seed(seed=1234)
    # alpha = 7
    # loc = 0
    # beta = 22

    # data = ss.gamma.rvs(alpha, loc=loc, scale=beta, size=100000)
    # data = loadData("tempIn.txt")
    data = loadData("InterarrivalTime.txt")
    # data = loadData("SerivceTime.txt")
    # data=[1, 1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 13, 13, 13, 14, 15, 15, 16, 16, 16, 16, 16, 17, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 21, 21, 21, 22, 22, 23, 23, 23, 24, 24, 24, 24, 25, 25, 25, 25, 26, 26, 27, 27, 27, 28, 28, 28, 29, 29, 30, 30, 31, 33, 34, 34, 35, 36, 36, 37, 37, 38, 38, 38, 39, 39, 40, 40, 42, 43, 43, 44, 44, 44, 44, 45, 45, 46, 46, 46, 46, 47, 50, 50, 51, 51, 51, 52, 52, 53, 53, 54, 55, 56, 57, 59, 60, 60, 62, 62, 63, 63, 64, 66, 67, 68, 69, 71, 72, 74, 74, 74, 74, 74, 75, 76, 77, 78, 78, 78, 78, 79, 79, 80, 80, 81, 81, 81, 82, 83, 84, 84, 85, 85, 86, 89, 89, 89, 91, 92, 93, 94, 94, 94, 94, 95, 95, 95, 97, 99, 100, 101, 102, 102, 104, 105, 106, 106, 107, 108, 109, 110, 111, 111, 112, 112, 112, 112, 114, 114, 115, 117, 118, 118, 118, 118, 124, 125, 125, 126, 128, 130, 132, 132, 132, 133, 134, 137, 141, 142, 145, 148, 150, 152, 152, 154, 157, 160, 160, 161, 164, 166, 166, 168, 175, 178, 181, 185, 185, 188, 197, 197, 201, 205, 205, 206, 207, 214, 223, 226, 227, 229, 233, 242, 243, 244, 244, 262, 268, 284, 294, 298, 306, 327, 332, 344, 349, 349, 363, 365, 370, 392, 405, 429, 442, 464, 517]
    
    print data
    #parameter estimation (in ss.gamma EX=alpha*beta, V(X)= alpha*beta*beta)!!!!
    fit_alpha, fit_loc, fit_beta = ss.gamma.fit(data, floc=0)
    rv = ss.gamma(fit_alpha, fit_loc, fit_beta)
    #fit_alpha, fit_loc = ss.expon.fit(data, floc=0)
    #rv = ss.erlang(fit_alpha, fit_loc)
    #rv = ss.expon(fit_alpha, fit_loc)
    # print "The parameters estimations are: k=%9.6f, loc(always)=%2d, lamda=%9.6f "%(fit_alpha+1, fit_loc, fit_beta)
    print "The parameters estimations are: alpha=%9.6f, loc(always)=%2d "%(fit_alpha, fit_loc)
    # k=int(1+math.log(266,2))
    k=int(1+math.log(327,2))
    # k=9
    # print k

    # set the adjustment to dof (degree of freedom) = to the number of parameters estimated
 
    dof=1
    # print 'dof: ',dof
    # chose the number of bins
    n=k
    print 'bin: ',n

##  experiment--------------------------------------------------
# create the histogram of the data for 100 bins
myHist = plt.hist(data, k, density=True)

# plot the density of this gamma rv
x = np.linspace(0.001,max(data)+10) 
h = plt.plot(x, rv.pdf(x), lw=2)

#show them together
plt.show() # if you want to see your picture uncomment this line

#produce pdf file myfig.pdf
# plt.savefig("myfig_service_time.pdf")
print model(data,n,dof)[1]
print "The chi_sq test value is %10.6f and the p-value is %10.6f" % (model(data, n, dof)[0], model(data,n,dof)[1])






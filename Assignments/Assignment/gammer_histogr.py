import numpy as np
import random
import scipy.stats as ss
import matplotlib.pyplot as plt

""" histogram of gamma data with pdf on the top"""
# generate gamma data
# scipy.stats generates gamma variates with mean = alpha*beta and
# variance = alpha*beta*beta

alpha, loc, beta = 7, 0, 22
data=np.loadtxt("data.csv", delimiter=',', skiprows=0)

#parameter fit based on the data and define gamma rv with these parameters
fit_alpha,fit_loc,fit_beta=ss.gamma.fit(data, floc=0)
rv = ss.gamma(fit_alpha,fit_loc,fit_beta)
#print fit_alpha,fit_loc,fit_beta 

# create the histogram of the data for 100 bins
myHist = plt.hist(data, 60, normed=True)

# plot the density of this gamma rv
x = np.linspace(0.001,500) 
h = plt.plot(x, rv.pdf(x), lw=2)

#show them together
#plt.show() # if you want to see your picture uncomment this line

#produce pdf file myfig.pdf
plt.savefig("myfig.pdf")

# Comments:
# 1). Read your data in
# 2). Estimate the parameters of the gamma distribution
#     to be fitted to your data 
# 3). Generate the histogram of your data
# 4). Save the histogram and the density as .ps or .pdf file
# 5). Print out or email this file to me

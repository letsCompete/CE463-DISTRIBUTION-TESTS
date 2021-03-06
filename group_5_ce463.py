# -*- coding: utf-8 -*-
"""Group 5 - CE463.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C9kfGnLYMOt7Xb2S2urZ6D9JQ5rYTAzT

# Q.1 Chi-Square Test for Exponential Distribution
"""

import math

"""Intervals in hours between failures of the air conditioning system of a Boeing 720 jet airplane"""

intervals = [23, 261, 87, 7, 120, 14, 62, 47, 225, 71, 246, 21, 42, 20, 5, 12, 120, 11, 3, 14, 71, 11, 14, 11, 16, 90, 1, 16, 52, 95]
print(intervals)

"""Sorting the intervals in ascending order"""

intervals.sort()
print(intervals)

"""Finding the sum of values and the mean value"""

n = len(intervals)
total = sum(intervals)
mean = total/n
print("n =",n, "\nsum of intervals =", total, "\nmean =", mean)

"""Dividing the intervals in 5 ranges including less than 15, 15-40, 40-65, 65-90, greater than 90"""

ranges = [[0,15], [15,40], [40, 65], [65, 90], [90, float("inf")]]
m = len(ranges)
print("m =", m, "\nranges =", ranges)

sets = []
sets.append(len([i for i in intervals if i<=15]))
sets.append(len([i for i in intervals if 15<i<=40]))
sets.append(len([i for i in intervals if 40<i<=65]))
sets.append(len([i for i in intervals if 65<i<=90]))
sets.append(len([i for i in intervals if i>90]))
sets

"""Given that the data follows an exponential distribution.
So, F(t) = 1-exp(-vt)
"""

v = n/total
print("Total number of occurences in a unit time, v =", v)

"""Finding the CDF of given distribution"""

CDF = []
for x in ranges:
    val = math.exp(-v*x[0]) - math.exp(-v*x[1])
    CDF.append(val)
print("CDF =",CDF)

"""Finding Theoretical frequencies, E, for m=5 intervals


"""

E = [n*val for val in CDF]
print("E =", E)

chisq = []
for i in range(m):
    val = ((sets[i]-E[i])**2)/E[i]
    chisq.append(val)
print("Chi-square =", chisq)

"""For exponential distribution, degree of freedom, f = m-1-k, where k is number of distribution paramters = 1 (for exponential distribution)"""

k = 1
f = m-1-k
chisq_f = sum(chisq)
print("f =",f, "\nChi-Square(f) =", format(chisq_f, "0.3f"))

"""For 5% level of significance, alpha = 0.05, we need to find critical value, C_(1-alpha,f) from the table"""

# For alpha = 0.05, 1-alpha = 0.95, and f = 3
c = 7.815
print("C_(1-alpha,f) =", c)

print("Chi-Square(f) =", format(chisq_f, "0.3f"), "and C_(1-alpha,f) =", c)
if c>chisq_f:
    print("Data is distributed exponentially at 5% level of significance as per Chi-Square Test")
else:
    print("Data is NOT distributed exponentially at 5% level of significance as per Chi-Square Test")

"""# Q.2 K-S Test

Data will be same as previous question
"""

print("We have intervals =", intervals, "n =", len(intervals))

"""CDF of observed samples, S[i] is calculated as rank/number of observations, i.e., m/n"""

S = [(i+1)/n for i in range(len(intervals))]
for i in range(len(intervals)):
    print("data =", intervals[i], "S[i] =", format(S[i], "0.3f"))

"""Finding thoeretical CDF of assumed distribution"""

n = len(intervals)
total = sum(intervals)
v = n/total
print("v =", v)

F = [1-math.exp(-v*intervals[i]) for i in range(n)]
for i in range(len(intervals)):
    print("data =", intervals[i], "S[i] =", format(S[i], "0.3f"), "F =", format(F[i], "0.3f"))

D = [abs(F[i] - S[i]) for i in range(n)]
for i in range(len(intervals)):
    print("S[i] =", format(S[i], "0.3f"), "data =", intervals[i], "F =", format(F[i], "0.3f"), "D =", format(D[i], "0.3f"))

D_n = max(D)
print("Max value of D =", format(D_n, "0.3f"))

"""We have 5% level of significance, So D(n_alpha) for alpha=0.05 is found using table"""

D_alpha = 0.242
print("D(n_alpha) =", D_alpha)

print("Max value of D_n =", format(D_n, "0.3f"), "and D_(n_alpha) =", D_alpha)
if D_n<=D_alpha:
    print("Data is distributed exponentially at 5% level of significance as per K-S Test")
else:
    print("Data is NOT distributed exponentially at 5% level of significance as per K-S Test")

"""# Q.3 Confidence Limits for mean density of concrete"""



"""# Q.4 Maximum Likelihood Method for Estimating Parameters of Normal Distribution"""

strength = [5.6, 5.3, 4.0, 4.4, 5.5, 5.7, 6.0, 5.6, 7.1, 4.7, 5.5, 5.9, 6.4, 5.8, 6.7, 5.4, 5.0, 5.8, 6.2, 5.6, 5.7, 5.9, 5.4, 5.1, 5.7]
n=len(strength)
print("n =",n)

"""We know that crushing strength follows Normal Distribution

Density function is:

f(x) = exp(-0.5 * (x-mu/sigma)^2))/ (sigma * sqrt(2 * pi))

We need differentiation of f(x) w.r.t sigma and mu to find out the mean and std deviation of the distribution.

After equating the derivations of f(x) w.r.t simga and mu to zero, we will get MLE for mu and sigma.

"""

mu = sum(strength)/n
squared = 0
for i in range(n):
  squared += (strength[i]-mu)**2
sigma = math.sqrt(((squared)/n))
print("Maximum Likelihood Estimation of mean, mu =", mu)
print("Maximum Likelihood Estimation of standard deviation, sigma =", format(sigma,"0.3f"))
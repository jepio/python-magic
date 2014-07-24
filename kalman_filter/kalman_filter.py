#!/usr/bin/env python2
## Implementing a Kalman Filter based on a Udacity course
import matplotlib.pyplot as plt
import numpy as np
import sys

def update(mean1, var1, mean2, var2):
    """ Measurement update """
    new_mean = (var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = (var1 ** -1 + var2 ** -1) ** -1
    return (new_mean, new_var)


def predict(mean1, var1, mean2, var2):
    """ Motion update """
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return (new_mean, new_var)

## Input data and initial estimates
m0 = 5
N = 25
if len(sys.argv) == 2:
    N = int(sys.argv[1])
measurements = (np.linspace(0, N - 1, num=N) +
                np.random.normal(loc=m0, scale=2., size=(N, )))
measurement_sig = 4.  # Let's see what happens when estimate is off
motion = np.random.normal(loc=1., scale=0.2, size=(N, ))
motion_sig = 0.3  # Same story

mu = 0
sig = 10

pred_mu = [mu]
pred_sig = [sig]

## 1D Kalman filter: update position and predict the next one
for i in range(N):
    mu, sig = update(mu, sig, measurements[i], measurement_sig)
    # print 'Update:',mu, sig
    mu, sig = predict(mu, sig, motion[i], motion_sig)
    # print 'Prediction', mu, sig
    pred_mu.append(mu)
    pred_sig.append(sig)

## Plot measurement and Kalman Filter
x = np.arange(0, N)
plt.figure(figsize=(6, 4))
plt.title("1D Kalman Filter")
plt.xlabel("Time",labelpad=-2)
plt.ylabel("Position")
plt.errorbar(x, measurements, label="Measurement")  # yerr=measurement_sig)
plt.errorbar(x, pred_mu[:-1], color='r', label="Estimate") #yerr=pred_sig[:-1])
plt.legend(*plt.gca().get_legend_handles_labels(), loc="upper left")
plt.savefig("kalman.png")  # dpi=200)

print "Final measurement covariance", pred_sig[-1]

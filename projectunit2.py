import numpy as np
   
# We are creating Binets Fibonacci Number contains n = 10 elements
# first 10 Fibonacci number


a = np.arange(1, 11)
lengthA = len(a)
  
# splitting of terms for easiness


sqrtFive = np.sqrt(5)
alpha = (1 + sqrtFive) / 2
beta = (1 - sqrtFive) / 2
  
# Implementation of formula
# np.rint is used for rounding off to integer
Fn = np.rint(((alpha ** a) - (beta ** a)) / (sqrtFive))

print("The first {} numbers of Fibonacci series are {} . ".format(lengthA, Fn))

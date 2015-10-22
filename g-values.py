#PROGRAM: g-values by Bonnie I. Kruft
# This program calculates the g-values of a paramagnetic sample by promping the user for the g-shifts.

import math

# prompts user for shifts

gxx = float(raw_input("What is the gxx shift relative to the free electron (ppm)? "))
gyy = float(raw_input("What is the gyy shift relative to the free electron (ppm)? "))
gzz = float(raw_input("What is the gzz shift relative to the free electron (ppm)? "))
GFE = float(2.0023193044)

# calculates g-values

gxx_value = gxx * float(.000001) + GFE  
gyy_value = gyy * float(.000001) + GFE
gzz_value = gzz * float(.000001) + GFE

# prints result

print "The g-values are: %f %f %f" % (gxx_value, gyy_value, gzz_value)







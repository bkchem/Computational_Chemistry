#PROGRAM: EPR by Bonnie Kruft
# This program calculates the g-values from the output of an EPR calculation.

from sys import argv

script, filename = argv

txt = open(filename)
searchlines = txt.readlines()
for i, line in enumerate(searchlines):
    if "   xx=         -" in line: 
        for l in searchlines[i:i+2]: 
	        l = line.split()
        	l1 = float(l[1])
		l2 = float(l[3])
		l3 = float(l[-1])
        print l1, l2, l3
txt.close()

GFE = float(2.0023193044)
gxx = l1
gyy = l2
gzz = l3

gxx_value = gxx * float(.000001) + GFE
gyy_value = gyy * float(.000001) + GFE
gzz_value = gzz * float(.000001) + GFE
print "The g-values are: %f %f %f" % (gxx_value, gyy_value, gzz_value)




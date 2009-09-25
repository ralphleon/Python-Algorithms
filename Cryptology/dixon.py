# dixon.py
# 
# Author: Ralph Gootee (rgootee@gmail.com)
#
# Uses dixon's method to factor a large number
#
# Example: 
#	factor(2231);
#
# TODO: Make a version that can run from the command line

from math import sqrt
from euclid import gcd

def factor(n):

	base = [2,3,5,7,11,13,17,19,23];

	start = int(sqrt(n))

	pairs = [];
	factors = [];
	for i in range(start,n):
		for j in range(len(base)):
			lhs = i**2 % n
			rhs = base[j]**2 % n

			if lhs == rhs: 
				print "%i^2 = %i = %i^2 = %i mod %i" % (i,lhs,base[j],rhs,n) 
				pairs.append([i,base[j]]);

	print "pairs:",pairs

	for i in range(len(pairs)):
		factor = gcd(pairs[i][0]-pairs[i][1],n)
		if(factor != 1): print "factor:",factor	

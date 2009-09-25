# euclid.py 
#
# Author: Ralph Gootee <ralph.gootee@jhuapl.edu>
#
# implementaions of the euclidean algorithm and the extended 
# euclidean algorithm
#

from math import floor;

#-------------------------------------------------------------------------------
def gcd(a,b):
	while b != 0:
		t = b;
		b = a % b;
		a = t;
	return a

#-------------------------------------------------------------------------------
def xgcd(a,b):

	x = 0;
	y = 1;
	lastx =  1;
	lasty = 0;

	while b != 0:

		temp = b;
		quotient = int(floor(a / b));
		b = a % b;
		a = temp;
		temp = x;
		x = lastx -quotient*x;
		lastx = temp;
		temp = y;
		y = lasty-quotient*y;
		lasty = temp;

	return [lastx,lasty];


# ss_prime.py
#
# Author: Ralph Gootee (rgootee@gmail.com)
#
# Solovay-Strassen primality test
#

## <snippet>

from random import random
import sys
#from euclid import gcd

#-------------------------------------------------------------------------------
def gcd(a,b):
	while b != 0:
		t = b;
		b = a % b;
		a = t;
	return a

#-------------------------------------------------------------------------------
def isPrime(n,k):
	
	if n % 2 == 0: return False;
 	pow = (n-1)/2;

	for i in range(k):

		a = int(random()*(n-1)) + 1;
	
	 	# modded by n to take care of the -1 case
		x = jacobi(a,n) % n;
		if x==0: return False;

		y = (a**pow) % n;
		if y % n != x % n: return False;

	return True;

#-------------------------------------------------------------------------------
def calc2(n):

	""" Case 4 """

	if n % 8 == 3 or n % 8 == 5: return -1;
	else: return 1;

#-------------------------------------------------------------------------------
def jacobi(n,m):

	""" Preforms the jacobi calculation """

	if gcd(n,m) != 1: return 0;

	negative = 1;

	while n > 1:

		# see if we should flip & mod 
		if m > n and n % 2 == 1 and m % 2 == 1:

			t = n; n = m; m = t;

			# test if negative
			m1 = n % 4;
			m2 = m % 4;

			if m1 == 3 and m2 == 3:
				negative *= -1;
			n = n % m;

		# see if we can extract a 2 
		elif n % 2 == 0:
			n = n/2;
			negative *= calc2(m);		
		
		else: 
			print "ERROR! degenerate case!";
			
	return negative;

## </snippet>

#-------------------------------------------------------------------------------
def main():
	
	if(len(sys.argv) != 2):
		print "Usage: ss_prime <integer>"
	else:
		val = int(sys.argv[1])
		print isPrime(val,5)

#-------------------------------------------------------------------------------
# to run the function if needed
if __name__ == "__main__":
    main();


# pohlig-hellman.py
#
# Author: Ralph Gootee
#
# TODO Make useable from the command line
#

from euclid import xgcd

def inv(x,p): return xgcd(x,p)[0];

def log(p,n,alpha,beta,q,c):
	""" Pohlig-Hellman

	"""
		
	j = 0
	B = [beta];
	for i in range(1,c+1):B.append(-1);

	a = [];
	for i in range(c):a.append(-1);

	while j <= c-1:

		q_j1 = q**(j+1)
		sigma = B[j]**(n/q_j1) % p;

		# find an i s.t. sigma = alpha^(in/q)
		
		for i in range(p):
			val = alpha**(i*n/q) % p;
			if sigma == val: 
				a[j] = i
				break

		if a[j] == -1: print "ERROR: No i found :("
		
		print "i: ", a[j]

		z = a[j] * q**j;
		
		alpha_inv = inv(alpha,p)
		alpha_inv_z = 1;	
		for i in range(z): alpha_inv_z = alpha_inv_z * alpha_inv 

		B[j+1] = B[j] * alpha_inv_z % p;
		j=j+1

	return a;


def test():

	p = 31;
	n = p-1;	
	alpha = 3;
	beta =12;

	a = log(p,n,alpha,beta,3,1);
	print "a:",a

	a = log(p,n,alpha,beta,5,1);
	print "a:",a

	a = log(p,n,alpha,beta,2,1);
	print "a:",a

	#print log(29,28,2,18,2,2)

test()


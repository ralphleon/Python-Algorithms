# pollard.py
#

from euclid import gcd

def f(x):
	""" function for pollard's rho """
	return x**2 + 1

def factor(n,b):
	""" Factor using Pollard's p-1 method """

	a = 2;
	for j in range(2,b):
		a = a**j % n
	
	d = gcd(a-1,n);
	print "d:",d,"a-1:",a-1
	if 1 < d < n: return d;
	else: return -1;

def factorRho(n,x_1):
	""" Factor using pollard's rho method """
	
	x = x_1;
	xp = f(x) % n
	p = gcd(x - xp,n)

	print "x_i's: {"
	while p == 1:
		print x,
		# in the ith iteration x = x_i and x' = x_2i
		x = f(x) % n
		xp = f(xp) % n
		xp = f(xp) % n
		p = gcd(x-xp,n)

	print "}"

	if p == n: return -1
	else: return p

def testFactor():
	
	print "Pollard's p-1 factoring"
	
	n = 13493
	s = 2
	d = -1

	print "n=%i, initial bound=%i" % (n,s)

	while s < n and d == -1:
		s +=1
		d = factor(n,s)
		print "Round %i = %i" % (s,d)

	if d == -1: print "No Factor could be found ..."
	else: print "%i has a factor of %i, with b=%i" % (n,d,s)

def testFactorRho():

	print "Pollard's Rho factoring" 
	n = 13493
	x_1 = 150

	print "n= %i, x_1= %i" % (n,x_1)
	
	p = factorRho(n,x_1)
	print "p=",p

testFactorRho();

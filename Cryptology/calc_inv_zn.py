# calc_inv_zn.py
#
# Author: Ralph Gootee
#
# Caluculates the modular inverse of x in Z_n. Used by many scripts in the 
# crypto suite.

import sys;

#-------------------------------------------------------------------------------
# euclidian algorithm
def euclidAlgorithm(a,b):
	while b != 0:
		t = b;
		b = a % b;
		a = t;
	return a

#-------------------------------------------------------------------------------
# Calculate the inverse elements in Z
def calcInvInZ(n):
	inv = [];
	for i in range(n):
		gcd = euclidAlgorithm(i,n);
		if gcd == 1: inv.append(i);
	return inv;

#-------------------------------------------------------------------------------
# calculates the inverse for an alement list inv. All inverse elements must
# actually exist in the list, for them to be inverses (closure)
def calcInv(inv,n):
	
	invPair = range(len(inv));

	for i in range(len(inv)):
		for j in range(len(inv)):
			value = (inv[i]*inv[j]) % n;
			if value == 1: invPair[i] = inv[j];
	return invPair;

#-------------------------------------------------------------------------------
def main():

	# calculate all of the inverses
	calcAll=0;

	for i in range(len(sys.argv)):
		if sys.argv[i] == "-i": calcAll=1;		
		if i+1 == len(sys.argv): n = int(sys.argv[i]);

	if n == -1: print "Usage: hw1.8.py [-i] <n>";
	
	print "Calculating inverses in Z_%i" % (n);
	inv = calcInvInZ(n);
	print "Inverses:",inv;

	if calcAll:
		invPair = calcInv(inv,n);

		for i in range(len(inv)): 
			print "(%i)^-1 = %i" % (inv[i],invPair[i]);  

# to run the function if needed
if __name__ == "__main__":
    main()

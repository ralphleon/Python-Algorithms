# Quadratic_residue.py
# 
# Author: Ralph Gootee (rgootee@gmail.com)
#

def calc(p):
	
	q = [];

	for i in range(p):
		val = i**((p-1)/2.0) % p;
		print "%i^{(%i-1)/2} = %i mod %i" % (i,p,val,p);
		if val == 1: q.append(i);

	return q;

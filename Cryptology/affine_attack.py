# affine_attack.py
#
# Author: Ralph Gootee <rgootee@gmail.com>
#

from calc_inv_zn import calcInvInZ,calcInv; 
from affine_cipher import affineCipherDecrypt;

def frequency(str):
	
	cNums = map(chr, range(65, 91));
	f = [];

	for i in range(len(cNums)):
		l = str.find(cNums[i],0);
		f.append(0);

		while l != -1:
			f[i] += 1;		
			l = str.find(cNums[i],l+1);

	return f;

def exh(str):

	cNums = map(chr, range(65, 91));
	inv = calcInvInZ(26);

	for a in inv:
		for b in range(len(cNums)):
			print "(%i,%i) %s" % (a,b,affineCipherDecrypt(str,a,b));			

def main():
	
	str = "PIIJCZHJUAZMVPMZZPVXELYMZPB";

	#f = frequency(str);
	#cNums = map(chr, range(65, 91));

	#print "String:", str, "length:",len(str);

	#for i in range(len(cNums)):
	#	print "cNums:", cNums[i], ", #",f[i]

	exh(str);

main();



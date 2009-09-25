# affine_cipher.py
#
# Author: Ralph Gootee (rgootee@gmail.com)

from calc_inv_zn import calcInvInZ,calcInv; 

import sys;

#-------------------------------------------------------------------------------
def affineCipherDecrypt(string,a,b):

	cNums = map(chr, range(65, 91));
	n = len(cNums);	

	decryptString = "";

	invElements = calcInvInZ(n);
	inv = calcInv(invElements,n);
	
	aInv = inv[invElements.index(a)];

	for c in string:
		decryptString += cNums[aInv*(cNums.index(c) - b) % n]; 

	return decryptString;

#-------------------------------------------------------------------------------
def affineCipherEncrypt(string,a,b):

	# remove all spaces from string
	string = string.replace(" ","");

	cNums = map(chr, range(65, 91));
	n = len(cNums);	

	encryptString = "";

	for c in string:
		encryptString += cNums[(a*cNums.index(c) + b) % n]; 

	return encryptString;

#-------------------------------------------------------------------------------
def main():

	if len(sys.argv) != 5:
		print "Usage: affine_cipher <decrypt|encrypt> string a b"
		exit();

	decrypt = 0;
	
	if sys.argv[1] == "decrypt":
		decrypt = 1 
	elif sys.argv[1] == "encrypt":
		decrypt = 0
	else: 
		print "The first argument is either 'encrypt' or 'decrypt'";
	
	str = sys.argv[2].upper();
	a = int(sys.argv[3]);
	b = int(sys.argv[4]);

	dStr = "";
	
	if decrypt: dStr = affineCipherDecrypt(str,a,b);
	else: dStr=affineCipherEncrypt(str,a,b);

	print "String:",str;
	print "-%s with K=(%i,%i)" % (sys.argv[1],a,b);
	print "Value:",dStr;

if __name__ == "__main__":
    main()



# book_spn.py
# 
# Author: Ralph Gootee (rgootee@gmail.com)
#
# TODO make references to book


subs = [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7];
perm = [1,5,9,13,2,6,10,14,3,7,11,15,4,8,12,16]; 

k = [ 	int("0011101010010100",2), 
		int("1010100101001101",2),
		int("1001010011010110",2),
		int("0100110101100011",2),
		int("1101011000111111",2) ];

def int2bin(n, count=24):
    """returns the binary of integer n, using count number of digits"""
    return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])

def inv(list):

	iList = [];

	for i in range(len(list)):
		iList.append(list.index(i));
	
	return iList;	
		

def pi_s(x,subs):

	str = int2bin(x,16);
	enc = "";

	# break the strings into blocks of 4	
	for i in range(4):
		strBlock = str[4*i:4*i+4];
		block = int(strBlock,2);
		trans = subs[block];
		#print "s: %i(%s) -> %i" % (block,strBlock,trans);
		enc += int2bin(trans,4);

	return int(enc,2);

def pi_p(x,perm):

	str = int2bin(x,16);
	enc = "";

	for i in range(len(str)):
		enc += str[perm[i]-1];
	
	return int(enc,2); 


def dec(y):

	# inverse the substitution list 
	invSubs = inv(subs);
	
	print "Inverse Substitution:",invSubs;

	n = len(k)-1;
	v = y ^ k[n];
	w = v;


	print "v4  - %s" % int2bin(v,16);
	print "K%i - %s" % (n+1,int2bin(k[n],16));
	
	for i in reversed(range(len(k)-1)):

		u = pi_s(v,invSubs);
		w = k[i] ^ u;
	
		# whiten with previous key
	
		print "v%i - %s" % (i+1,int2bin(v,16));
		print "u%i - %s" % (i+1,int2bin(u,16));
		print "K%i - %s" % (i+1,int2bin(k[i],16));
		print "-------";		
		print "w%i - %s" % (i,int2bin(w,16));
	

		v = pi_p(w,perm);

	return w;

def enc(x):

	w = x;
	u = 0;

	for i in range(len(k)-1):
	
		# exclusive or	
		u = w ^ k[i];
		
		v = pi_s(u,subs);
		
		print "w%i - %s" % (i,int2bin(w,16));
		print "K%i - %s" % (i+1,int2bin(k[i],16));
		print "u%i - %s" % (i+1,int2bin(u,16));
		print "v%i - %s" % (i+1,int2bin(v,16));
		print "--------";

		w = pi_p(v,perm);

	n = len(k)-1;
	y = v ^ k[n];
	print "K%i - %s" % (n,int2bin(k[n],16));
	return y;


def main():

	#x = int("1011110011010110",2);
 	#y = enc(x);

	#print "y  - %s" % int2bin(y,16);

	y = int("0010011010110111",2);
 	x = dec(y);

	print "x  - %s" % int2bin(x,16);




main(); 


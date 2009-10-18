#!/bin/python
#
# First attempt at a SHA1 algorithm in python
#
# Author: rgootee@gmail.com

import array
from math import floor
import sys

N = 	0x100000000;
MASK = 	0xFFFFFFFF;

def leftRotate(word, n):
	return ((word<<n)&MASK)|(word>>32 - n)

def add(A,B):
	return (A + B) % N

def sha1Hash(stringArray):

	l = len(stringArray)*8

	# Append a 1 to the beginning 
	stringArray.append(0x80);

	# Fill in the zeros so that it's 448 % 512 
	# (remember:) there are already 7 zeros in 1's bucket)
	nZeros = ( 448 - (len(stringArray))*8) % 0x200
	boxes = int(floor(nZeros/8));

	print ("Filling in %i zeros (boxes=%i) ...") % (nZeros,boxes)

	for i in range(boxes): stringArray.append(0);

	# Assume that the size is < 2^32
	stringArray.append(0)
	stringArray.append(0)
	stringArray.append(0)
	stringArray.append(0)

	stringArray.append(0)
	stringArray.append(0)
	stringArray.append(0)
	stringArray.append(l)

	# A chunk is 1 words == 4 arrays, 16 words = 64
	n = len(stringArray)/ 64

	h0 = 0x67452301
	h1 = 0xEFCDAB89
	h2 = 0x98BADCFE
	h3 = 0x10325476
	h4 = 0xC3D2E1F0

	for i in range(n):
				
		startOfChunk = i*64
		w = [0]*80
		
		# Divide m into 16 words
		for i in range(16):
			
			val = 0;

			for x in range(4):
				cell = stringArray[startOfChunk + 4*i + x]
				val = val << 8
				val |=cell
					
			w[i] = val
	
		# Add more 
		for t in range(16,80):
			w[t] = leftRotate((w[t-3] ^ w[t-8] ^ w[t-14] ^ w[t-16]),1)

		A = h0
		B = h1
		C = h2
		D = h3
		E = h4

		for t in range(80):

			if t < 20:
				K = 0x5a827999
				f = (B & C) | ((B ^ 0xFFFFFFFF) & D)
			elif t < 40:
				K = 0x6ed9eba1
				f = B ^ C ^ D
			elif t < 60:
				K = 0x8f1bbcdc
				f = (B & C) | (B & D) | (C & D)
			else:
				K = 0xca62c1d6
				f = B ^ C ^ D

			temp = (leftRotate(A,5) + f + E + w[t] + K) & 0xFFFFFFFF;

			E = D
			D = C
			C = leftRotate(B,30)
			B = A
			A = temp 

			#print t,":","A",hex(A),"B",hex(B)
			#print "C",hex(C),"E",hex(E),"D",hex(D),"E",hex(E)

		h0 = add(h0,A)
		h1 = add(h1,B)
		h2 = add(h2,C)
		h3 = add(h3,D)
		h4 = add(h4,E)

		print "Digest", hex(h0),hex(h1),hex(h2),hex(h3),hex(h4)	

def main():

	if(len(sys.argv) < 2):
		print "usage: sha1 <Text Message>"
	else: 
		stringMsg = sys.argv[1] 
		stringArray = []

		for byte in array.array('B', stringMsg): stringArray.append(byte)
		sha1Hash(stringArray)

if __name__ == "__main__":
    main()

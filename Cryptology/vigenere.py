# vignere.py
#
# author: Ralph Gootee <rgootee@gmail.com>
#

import sys # for command line arguments
import os # to see if a file exists
import vigenere_attack

#-------------------------------------------------------------------------------
def Decrypt(string,passkey):
	
	cNums = map(chr, range(65, 91));
	m = len(passkey);

	newString = "";

	for i in range(len(string)-1):
		iString = cNums.index(string[i]); 
		iPass =  cNums.index(passkey[i % m]);
		value = (iString - iPass) % len(cNums);
		newString += cNums[value];
	
	return newString;

#-------------------------------------------------------------------------------
def Encrypt(string,passkey):
	
	cNums = map(chr, range(65, 91));
	m = len(passkey);

	newString = "";

	for i in range(len(string)):
		iString = cNums.index(string[i]); 
		iPass =  cNums.index(passkey[i % m]);
		value = (iString + iPass) % len(cNums);
		newString += cNums[value];
	
	return newString;

#-------------------------------------------------------------------------------
def Main():

	""" Main function """

	verbose =0;
	file = "";
	passkey = "";
	encrypt = 0;
	

	if (len(sys.argv) < 2):
		print "usage: vigenere.py [encrypt|decrypt] [-v] [-p passcode] <file>";
		exit();

	if sys.argv[1] == "encrypt": encrypt = 1;
	elif sys.argv[1] == "decrypt": encrypt = 0;
	else: 
		print "unknown option \"",sys.argv[1],"\", must be encrypt or decrypt";

	#parse command line arguments 	
	for i in range(2,len(sys.argv)): 
		if sys.argv[i] == "-v": 
			verbose = 1
		
		elif sys.argv[i] == "-p":
			passkey = sys.argv[i+1]
		
		elif i+1 == len(sys.argv):
			file = sys.argv[i];

	string = vigenere_attack.ParseXMLFile(file);

	#remove all newlines from string
	string = string.replace('\n','');	
	string = string.replace(' ','');	
	
	print "Passkey: ",passkey;

	if encrypt:
		encrypt = Encrypt(string,passkey);
		print "Encrypt: ",encrypt;
	else:
		print "Decrypt Mode:"
		decrypt = Decrypt(string,passkey);
		print "Decrypt: ",decrypt;

#-------------------------------------------------------------------------------
# to run the function if needed
if __name__ == "__main__":
    Main();


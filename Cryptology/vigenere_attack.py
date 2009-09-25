# kasiski_attack.py
#
# Author: Ralph Gootee <rgootee@gmail.com>
#

#-------------------------------------------------------------------------------
from xml.dom.minidom import parse # used for xml parsing
import sys # for command line arguments
import os # to see if a file exists

#-------------------------------------------------------------------------------
# euclidian algorithm
def gcd(a,b):
	while b != 0:
		t = b;
		b = a % b;
		a = t;
	return a

#-------------------------------------------------------------------------------
def GcdArray(gcdz):

	""" Takes the greatest common divisor of an entire array """

	if len(gcdz) < 2: return gcdz[0];
	
	myGcd = gcd(gcdz[0],gcdz[1]);	

	for i in range(2,len(gcdz)):
		myGcd = gcd(gcdz[i],myGcd);

	return myGcd;

#-------------------------------------------------------------------------------
def ParseXMLFile(file):

	"""Parses a xml file and runs the core of the string matcher on the results

	Keyword Arguments:
	file -- the file name with which to parse
	
	"""

	string = "";

	# reads in the dom structure
	dom = parse(file);	

	# generate touples
	for node in dom.getElementsByTagName('string'): 
		string = node.firstChild.nodeValue;
	
	print "XML File: ", file;
	print "String: ", string;

	return string;

#-------------------------------------------------------------------------------
def CalcKeyLength(string,gramLength,verbose=0):

	""" Calculates the suggested passkey length of the string using Kasiski """

	locations = [];
	distances = [];

	#locate all grams
	for i in range(len(string)):
		gram = string[i:i+gramLength];
		
		# make sure we don't get stuck with shorties
		if len(gram) < gramLength: break
	
		locations.append([]);

		find = string.find(gram,0);
		while find != -1:
			locations[i].append(find);
			find = string.find(gram,find+1);
	
		# only calculate the distances if need be
		if len(locations[i]) > 1:
			for j in range(1,len(locations[i])):
				distances.append(locations[i][j] - locations[i][0]);

			if verbose: print "gram: ",gram;
			if verbose: print "found: ", locations[i];

	if verbose: print "distances: ", distances;
	
	myGcd = GcdArray(distances);	

	return myGcd;

#-------------------------------------------------------------------------------
def ConstructY(string,m):

	""" 
		Constructs the Y_i vectors of string 

		Input Arguments:
		string -- the ciphertext
		m -- the passkey length
	
	"""

	# figure this out
	y = [];
	for i in range(m):y.append('');

	for i in range(len(string)):
		index = i % m;
		y[index] += string[i];

	return y;
				
#-------------------------------------------------------------------------------
def CalcMg(y):

	""" calculates the M_g value for a given string vector """	
	
	cNums = map(chr, range(65, 91));

	mg = [];
	f = range(len(cNums));

	p = [.082,.015,.028,.043,.127,.022,.020,.061,.070,.002,.008,.040,.024,.067];
	p+=	[.075,.019,.001,.060,.063,.091,.028,.010,.023,.001,.020,.001];

	#print "p=",p;

	# frequency & probabiliy
	for i in range(len(cNums)):
		f[i] = y.count(cNums[i]);	
		mg.append(0);

	#print "f:",f;
	
	for g in range(len(cNums)):
		for i in range(len(cNums)):
			fig = f[(i+g)% len(f)];
			mg[g] += ((p[i]*fig) / float(len(y)));

	#print "mg: ", mg;
	return mg;

#-------------------------------------------------------------------------------
def SuggestKey(mg):
	
	""" Suggestes a key, given the maximum likelihood """

	contend = [];
	cNums = map(chr, range(65, 91));

	i = max(mg);
	return cNums[mg.index(i)];

#-------------------------------------------------------------------------------
def Attack(string,n,verbose=0):
	
	# construct y[i]
	y = ConstructY(string,n);
	if verbose:
		for i in range(n): print 'y(%i): %s' % (i,y[i]);

	mg = [];
	# calculate Mg
	for i in range(n): 
		m = CalcMg(y[i]);
		mg.append(m);
		if verbose: print "M_g(y[i])=",m;		

	# suggest the key
	key = "";
	for i in range(n):
		key += SuggestKey(mg[i]);

	return key;

	
#-------------------------------------------------------------------------------
def Main():

	""" Main function """

	print "Vigenere Cipher Attack";

	verbose =0;
	file = "";
	gramLength = 4;
	keyLength = 0;

	#parse command line arguments 	
	for i in range(1,len(sys.argv)): 
		if sys.argv[i] == "-v": 
			verbose = 1
		if sys.argv[i] == "-g": 
			gramLength = int(sys.argv[i+1]);
		if sys.argv[i] == "-k": 
			keyLength = int(sys.argv[i+1]);
		if i+1 == len(sys.argv):
			file = sys.argv[i];
	
	string = ParseXMLFile(file);
	#remove all newlines from string
	string = string.replace('\n','');	
	string = string.replace(' ','');	

	if( keyLength == 0):
		print "Gram Length: ",gramLength;
		keyLength = CalcKeyLength(string,gramLength,verbose);
		
	if verbose: print "Key Length:", keyLength;
		
	passkey = Attack(string,keyLength,verbose);
	print "Suggested Passkey:",passkey


#-------------------------------------------------------------------------------
# to run the function if needed
if __name__ == "__main__":
    Main();


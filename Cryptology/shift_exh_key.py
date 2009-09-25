# shift exhaustive search 
#
# Author: Ralph Gootee
# 
# hw1.5.py
# exhaustive key search 
#
# TODO	make into a function
#		make a command line version

string = "RQOBMXOLXVXVHGWKLVFLSKHU"

cNums = map(chr, range(65, 91));

print "Brute Force Exhaustive Search, 1.5"

# loop through all 26 keys
for i in range(26):
	
	newString = "";

	#loop through all characters
	for s in string:
		num = (cNums.index(s) + i) % len(cNums);
		newString += cNums[num];
	
	print "Key %02i : %s" % (i,newString);


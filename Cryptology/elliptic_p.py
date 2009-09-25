from euclid import xgcd
import pdb

def points(p):

	for i in range(p):
		x = (i**3 + i + 4) % p
		q = qr(x,p)
		if q: 
			y = sqrt(x,p)
			print "%i) x=%i qr=%i y = (%i,%i)" % (i,x,q,y[0],y[1])

def qr(x,p):

	if x**((p-1)/2) % p == 1: return 1
	else: return 0

def add(p,q,n):

	a = 1
	lamda = 0;

	if p == q:
		lamda = (3*p[0]**2 + a) * xgcd(2*p[1],n)[0]
	else: 
		lamda = (q[1] - p[1]) * xgcd(q[0] - p[0],n)[0] 

	lamda = lamda % n

	x3 = (lamda**2 - p[0] - q[0]) % n
	y3 = (lamda*(p[0] - x3) - p[1]) % n

	return [x3,y3]

def multiples(alpha,p,n):
	
	a = 1;
	sum = alpha;

	for i in range(1,n+1):
		
		print "%i X (%i,%i) = (%i,%i)" % (i,alpha[0],alpha[1],sum[0],sum[1])
		sum = add(sum,alpha,p)

def sqrt(x,p):
	
	y = []

	if p % 4 == 3:
		val = x**((p+1)/4)
		y.append( val % p)
		y.append( -val % p)
	
	return y;

def test():

	p = 23
	#points(p)
	#multiples([0,2],23,23)
	#multiples([8,3],11,7)
	multiples([15,6],23,9)

if __name__ == "__main__":
	test()

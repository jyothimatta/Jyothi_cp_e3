# Bisection Algorithm comes into play!
# We know that the square root of x lies between 1 and x, from mathematics
# Rather than exhaustively trying things starting at 1, suppose instead we pick a number in the middle of this range
# Bisection search works when value of function varies monotonically with input
# If g, the users input/guess, is less than/greater than the midpoint of the range, then that number becomes the new high point of said range and is then factored into the new search.

def ofEqualSign(a,b):
    return (a * b) > 0

def findzerowithbisection(f,x0,x1, epsilon):
	if ofEqualSign(f(x0),f(x1)):
		return None
	else:
		xmid = (x1+x0)/2
		ymid = f(xmid)
		if ymid == 0 or abs(ymid) < epsilon:

			return xmid
		elif ymid > 0:
			return findzerowithbisection(f, x0, xmid, epsilon)
		else:
			return findzerowithbisection(f, xmid, x1, epsilon)
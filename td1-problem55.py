
def reverse(n):
	rev = 0

	while n!=0:
		rev*=10
		rev+= n%10
		n//=10

	return rev

def isLychrel(n):
	
	for i in range(50):
		n+= reverse(n)
		if(reverse(n)==n):
			return False
	return True

def solve():

	l_count = 0
	for i in range(0, 10**4):
		if isLychrel(i):
			l_count +=1

	return l_count

print(solve())

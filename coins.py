# script to solve coin problem
# Returns: 9,2,5,7,3

from itertools import permutations

coins = [2,3,5,7,9]

# takes a list of coins, ls, and a fragmented
	
def trySolution(p):
	a,b,c,d,e = p[0],p[1],p[2],p[3],p[4]
	return a + (b*(c**2)) + d**3 - e == 399

def main():
	perms = permutations(coins)
	for p in perms:
		if trySolution(p):
			for i in p: print(i,end=" ")
			print()
			break

if __name__=="__main__":
	main()

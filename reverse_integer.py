# last digit is the remainder when we %10 and to remove that digit from number /10
def rev_integer(n):
	reversed=0
	remainder=0
	while n>0:
		remainder=n%10
		n=n/10
		reversed=reversed*10+remainder
	return reversed

if __name__=="__main__":
	print(rev_integer(3461))
def is_palindrome(string):
	rev_string=string[::-1]
	if string==rev_string:
		return True
	else:
		return False
if __name__=="__main__":
	str="radarrr"
	if is_palindrome(str):
		print("Is palindrome")
	else:
		print("Not palindrome")

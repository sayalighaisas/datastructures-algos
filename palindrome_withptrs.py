def is_palin(input_string):
	start=0
	end=len(input_string)-1
	while start<end:
		if input_string[start]!=input_string[end]:
			return False
		start+=1
		end-=1
	return True


if __name__=="__main__":
	str="dad"
	if is_palin(str):
		print("is palindrome")
	else:
		print("not palindrome")

#Finding duplicates in an array where values of all integers are lesser that the length of array(imp)
#bruteforce: compare every elem to every other elem viz O(N2)
#Can use dictionary(hash) but requires additional memory
#algo to do in O(n) RT and in-place uses absolute values

def duplicates(nums):
	for num in nums:
		if nums[abs(num)]>=0:
			nums[abs(num)]=-nums[abs(num)]    #flip the sign of the value at that position if already flipped value is encountered back its repetition
		else:
			print("repetition found", abs(num))

if __name__ == "__main__":
	nums=[2,6,3,5,4,2,3]
	duplicates(nums)
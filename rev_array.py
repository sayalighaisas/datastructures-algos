#Method1: use slice notation
#a=[1,2,3,4,5]
#b=a[::-1]
#print(b)
#Method2: use 2 pointers at start and end and swap.
def reverse(nums):
	start_index=0
	end_index=len(nums)-1
	while start_index<end_index:
		nums[start_index], nums[end_index]= nums[end_index], nums[start_index]
		start_index+=1
		end_index-=1

	return nums

if __name__=="__main__":
	nums=[1,2,3,4,5]
	print(reverse(nums))


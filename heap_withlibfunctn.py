from heapq import heappush, heappop, heapify
# Operation 1: heapify is to build the heap (we use array representation)
# Default forms a min heap. Python builds a min heap
heap=[]
nums=[12,3,-2,6,4,8,9]

heapify(nums)
print(nums)

# Operation 2: heapsort with push and pop: will return ascending order
for num in nums:
	heappush(heap,num)

while heap:
	print(heappop(heap))

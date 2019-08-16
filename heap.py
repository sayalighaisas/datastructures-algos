CAPACITY = 10

class Heap(object):

	def __init__(self):
		self.heap=[0]*CAPACITY
		self.heapsize=0

	def insert(self,item):
		if CAPACITY==self.heapsize:
			return

		# insert item at array index=heap_size(0,1,2..)
		self.heap[self.heapsize]=item
		self.heapify(self.heapsize)
		# print(self.heap)
		self.heapsize=self.heapsize+1


	def heapify(self, index):   #o(logN)
		parent_index=(index-1)//2
		if index>0 and self.heap[index]>self.heap[parent_index]:
			self.swap(index,parent_index)
			self.heapify(parent_index)


	def swap(self, index, parent_index):
		self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]

	def getmax(self):   #max-heap 0(1)
		return self.heap[0]

	# Heapsort implementation:
	# remove max root elem and replace with last element
	def poll(self):
		max=self.getmax()
		self.swap(0, self.heapsize-1)
		self.heapsize=self.heapsize-1
		self.fixdown(0)
		return max
	# fix rest of the heap values
	def fixdown(self, index):   # TC: 0(logN)
		index_left = 2*index+1
		index_right = 2*index+2
		index_largest = index

		if index_left<self.heapsize and self.heap[index_left]>self.heap[index]:
			index_largest=index_left

		if index_right<self.heapsize and self.heap[index_right]>self.heap[index_largest]:
			index_largest=index_right

		if index!=index_largest:
			self.swap(index,index_largest)
			self.fixdown(index_largest)
	#run the above for all N heap elements TC:O(NlogN)
	def heapsort(self):
		size=self.heapsize
		for i in range(0,size):
			max=self.poll()
			print(max)



if __name__ == "__main__":
	heap = Heap()
	heap.insert(10)
	heap.insert(-20)
	heap.insert(0)
	heap.insert(2)
	heap.insert(4)
	heap.insert(5)

	heap.heapsort()


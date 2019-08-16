class Queue(object):
	def __init__(self):
		self.queue=[] #implement queue as list

	def isEmpty(self):
		return self.queue==[]

	def enqueue(self,data):
		self.queue.append(data)

	def dequeue(self):
		data=self.queue[0]  #FIFO
		del self.queue[0]
		return data

	def peek(self):
		return self.queue[0]

	def sizeQ(self):
		return len(self.queue)

queue=Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.sizeQ())
print(queue.dequeue())
print(queue.dequeue())
print(queue.sizeQ())

while not (queue.isEmpty()):
	print(queue.peek())
	queue.dequeue()
print("Queue Empty!")
queue.enqueue(25)
print(queue.sizeQ())

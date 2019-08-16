class Stack():
	def __init__(self):
		self.stack=[]   #implement stack as list

	def isEmpty(self):
		return self.stack==[]

	def push(self,data):
		self.stack.append(data)

	def pop(self):
		data = self.stack.pop() #pop() is self.stack[-1] and del self.stack[-1]
		return data

	def peek(self):   #reads the TOS
		return self.stack[-1]


stack=Stack()
stack.push(1)
stack.push(2)
stack.push(3)
while not (stack.isEmpty()):
	print("TOS:",stack.peek())
	print("Popped:",stack.pop())

print("Stack emty!")
stack.push(4)
print("TOS:",stack.peek())







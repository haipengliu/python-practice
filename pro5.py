#5.ջ(Stack)��һ���������б�����ݽṹ�������б�������ǣ�1�������µ�������ֻ�ܼӵ�ĩβ��(2)��ȡ�ṹ�е�������ֻ�ܴ�ĩβ���С���Pythonʵ��һ��Stack�࣬ʵ��Push()��Pop()����������

class Stack:
	def __init__(self,size):
		self.stack = []
		self._size = size
		self._next = -1
	def setSize(self, size):
		self._size = size
	def isEmpty(self):
		if self._next == -1:
			return True
		else:
			return False
	def isFull(self):
		if self._next + 1 == self._size:
			return True
		else:
			return False
	def getValue(self):
		if self.isEmpty():
			raise Exception("StackIsEmpty")
		else:
			return self.stack[self._next]
	def push(self, obj):
		if self.isFull():
			raise Exception("StackOverFlow")
		else:
			self.stack.append(obj)
			self._next += 1
	def pop(self):
			if self.isEmpty():
				raise Exception("StackIsEmpty")
			else:
				self._next -= 1
				return self.stack.pop()
	def show(self):
		print(self.stack)

s = Stack(5)
s.push(1)
s.push(2)
s.push(3)
s.show()
s.pop()
s.show()
s.push(6)
s.show()

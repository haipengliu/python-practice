#7.	ʵ��һ�������Ķ������㷨��
class Heap:
	def __init__(self, arr_in):
		arr = arr_in
		arrlen = len(arr)
		for i in reversed(range(0, (arrlen-1)/2)):
			heap_adjust(arr, i, arrlen-1)
	
	def heap_adjust(arr, low, high):
		left = low*2+1
		right = left+1
		current = low //������ָ��ô��
		
		temp = arr[dad]
		
		while left 
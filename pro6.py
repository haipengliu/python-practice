#6.	给定一组整数[12,34,45,23,45,56,12,12,34]，把数字按出现的次数排序。

class NumInfo:
	def __init__(self):
		self.num = ''
		self.count = 0

def num_count_cmp(n1, n2):
	return 0-cmp(n1.count, n2.count)

_list = [12,34,45,23,45,56,12,12,34]
_list_sort = []

_map = {}

for num in _list:
	if _map.get(num) == None:
		_map[num] = 1
	else:
		_map[num] += 1

for num in _map.keys():
	ni = NumInfo()
	ni.num = num
	ni.count = _map[num]
	_list_sort.append(ni)

_list_sort.sort(num_count_cmp)

print 'The sorted list according to the number occurences is:\n'
for x in _list_sort:
	print str(x.num)+' : '+str(x.count)+'\n'

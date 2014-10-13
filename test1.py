#1. 给定一个字符串列表 ['abcdz',’aez’,'bacde','bcadxxxx','cdbagg','abdcttttttttt']，
#实现一个Python程序，输出按照从后到前的字母排序的结果，要求按照降序排列。
#例如’ abcdz’的最后一个字母是’z’，'bcadxxxx'的最后一个字母是’x’，
#因此’ abcdz’应该排在'bcadxxxx'前面；’ abcdz’和’aez’最后一个字母相同，但后者倒数第2个字母较大，应排在前面。

class TermInfo:
	def __init__(self):
		self.term = ''
		self.sec = '' #second letter

def term_info_cmp(t1,t2):
	return cmp(t1.sec,t2.sec)
	
list_temp = ['abcd','bacd','bcad','cdba','abdc']
print 'The original list is :'
for x in list_temp:
        print x+'\n'

list_cls = []

for x in list_temp:
	y = TermInfo()
	y.term = x
	y.sec = y.term[1]
	list_cls.append(y)
	
list_cls.sort(term_info_cmp)

print 'The result sorted by the second letter is:\n'
for x in list_cls:
	print x.term+'\n'

# 4.	给定一个字符串列表 ['abcd','bacd','bcad','cdba','abdc']，要求输出按照第2个字母排序的结果。例如'abcd'的第2个字母是b，'bacd'的第2个字母是a，因此'bacd' < 'abcd'。

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

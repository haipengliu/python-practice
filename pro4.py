# 4.	����һ���ַ����б� ['abcd','bacd','bcad','cdba','abdc']��Ҫ��������յ�2����ĸ����Ľ��������'abcd'�ĵ�2����ĸ��b��'bacd'�ĵ�2����ĸ��a�����'bacd' < 'abcd'��

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

#1. ����һ���ַ����б� ['abcdz',��aez��,'bacde','bcadxxxx','cdbagg','abdcttttttttt']��
#ʵ��һ��Python����������մӺ�ǰ����ĸ����Ľ����Ҫ���ս������С�
#���硯 abcdz�������һ����ĸ�ǡ�z����'bcadxxxx'�����һ����ĸ�ǡ�x����
#��ˡ� abcdz��Ӧ������'bcadxxxx'ǰ�棻�� abcdz���͡�aez�����һ����ĸ��ͬ�������ߵ�����2����ĸ�ϴ�Ӧ����ǰ�档

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

#3.	����һ���ַ����б� ['abc 123','abc123','bcdef','ef ghi@#','XYZ000pqm']���ҳ����н�����Ӣ����ĸ�����ֵ��ַ�����

import re

pattern = re.compile(r'[a-zA-Z0-9]+')

str_list = ['abc 123','abc123','bcdef','ef ghi@#','XYZ000ѧϰpqm']

print 'The string containing only letters or numbers are:\n'
for x in str_list:
	match = pattern.findall(x)
	if len(match) == 1 :
		if len(match[0]) == len(x):
			print x+'\n'


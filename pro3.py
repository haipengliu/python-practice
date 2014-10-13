#3.	给定一个字符串列表 ['abc 123','abc123','bcdef','ef ghi@#','XYZ000pqm']，找出所有仅包含英文字母和数字的字符串。

import re

pattern = re.compile(r'[a-zA-Z0-9]+')

str_list = ['abc 123','abc123','bcdef','ef ghi@#','XYZ000学习pqm']

print 'The string containing only letters or numbers are:\n'
for x in str_list:
	match = pattern.findall(x)
	if len(match) == 1 :
		if len(match[0]) == len(x):
			print x+'\n'


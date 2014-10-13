#1.	给定一个字符串列表 ['the last time','the first time','the best time','the worst time','the best student','the worst record']，找出其中包含best的所有字符串。

str_list = ['the last time','the first time','the best time','the worst time','the best student','the worst record']

term = 'best'

print 'The string which contains \'best\' are: \n'
for x in str_list:
	if term in x:
		print x+'\n'
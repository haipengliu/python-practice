#2.	给定一个字符串列表 ['abcd','test','efgh','abcd','test','ghijk','xyz']，要求输出所有不同的字符串及其在列表中出现的次数，例如'abcd'在列表中出现了2次，'xyz'出现了1次，等。

str_list = ['abcd','test','efgh','abcd','test','ghijk','xyz']

map_temp = {}

for x in str_list:
	if map_temp.get(x) == None:
		map_temp[x] = 1
	else:
		map_temp[x] = map_temp[x]+1

for y in map_temp.keys():
	print y+'	'+':' +str(map_temp[y])+'\n'
#2.	����һ���ַ����б� ['abcd','test','efgh','abcd','test','ghijk','xyz']��Ҫ��������в�ͬ���ַ����������б��г��ֵĴ���������'abcd'���б��г�����2�Σ�'xyz'������1�Σ��ȡ�

str_list = ['abcd','test','efgh','abcd','test','ghijk','xyz']

map_temp = {}

for x in str_list:
	if map_temp.get(x) == None:
		map_temp[x] = 1
	else:
		map_temp[x] = map_temp[x]+1

for y in map_temp.keys():
	print y+'	'+':' +str(map_temp[y])+'\n'
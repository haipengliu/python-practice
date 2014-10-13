import os

class TermInfo:
	def __init__(self):
		self.term = ""
		self.count = 0

def term_info_cmp(t1,t2):
	return 0-cmp(t1.count,t2.count)

map = {}

file = open('out_all.txt')

content = file.readlines()

file.close()

for line in content:
	line = line.strip()
	if map.get(line) == None:
		map[line] = 1
	else:
		map[line] = map[line]+1


list_term_info = []
for term in map.keys():
	ti = TermInfo()
	ti.term = term
	ti.count = map[term]
	list_term_info.append(ti)
	
list_term_info.sort(term_info_cmp)	

output = open('out_all_deduplicated.txt','w')

for ti in list_term_info:
	output.write(ti.term+'\t'+str(ti.count)+'\n')

output.close()

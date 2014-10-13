f1 = open('arctic100.dic')
f2 = open('0535.dic')

ct1 = f1.readlines()
ct2 = f2.readlines()

f1.close()
f2.close()

dict1 = {}
dict2 = {}

for line in ct1:
	line = line.strip()
	tline = line.split('\t')
	term = tline[0]
	pron = tline[1]
	dict1[term] = pron

for line in ct2:
	line = line.strip()
	tline = line.split('\t')
	term = tline[0]
	pron = tline[1]
	dict2[term] = pron


for term in dict2.keys():
	if term not in dict1.keys():
		dict1[term] = dict2[term]

f3 = open('arctic100_merged.dic','w')
for term in dict1.keys():
	f3.write(term+'\t'+dict1[term]+'\n')	

f3.close()

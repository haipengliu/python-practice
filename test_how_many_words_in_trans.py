# This python script is for testing how many generated sas terminology words are included in the original transcriptions

#Input: file1 - recognized results(composed using sas terminology items)
#       file2 - orignial transcriptions text
#Output: included words and their occurances

#TAG haipeng

import operator

file1=open('live_result.txt')
ct_1=file1.readlines()
file1.close()

result_dict={}
#filter the result_dict with stop words
sw_dict={} #stop words dict
file_sw=open('/kaldi/SAS_LM/en.iso8859-1.stopwords.txt')
ct_sw=file_sw.readlines()
file_sw.close()
for line in ct_sw:
    tline=line.strip()
    sw_dict[tline]=2

    




for line in ct_1:
    line_1=line.strip()
    line_2=line_1.split(' ')
    for term in line_2:
        if result_dict.get(term)==None:
            result_dict[term]=1
        else:
            result_dict[term]=result_dict[term]+1

file2=open('Andy_tran9.txt')
ct_2=file2.readlines()
file2.close()

result_statistics={}

for line in ct_2:
    line_1=line.strip()
    line_2=line_1.split(' ')
    for word in line_2:
        if result_dict.get(word)!=None:
            if result_statistics.get(word)==None:
                result_statistics[word]=1
            else:
                result_statistics[word]=result_statistics[word]+1


sorted_stat=sorted(result_statistics.iteritems(),key=operator.itemgetter(1))

file3=open('how_many_sasterm_in_trans.txt','w')
#pairs=result_statistics.items()
for line in sorted_stat:
    (key, val)=line
    file3.write(key+'\t'+str(val)+'\n')
file3.close()

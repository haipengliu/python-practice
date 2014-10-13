#This script compares two transcription, but only compare the words filtered by sas terminology list
#Input: recognized transcription, human labeled transcription, sas terminology list
#Output:correct rate of recognized sas term (correct counts/total occurance counts)
#TAG Haipeng

#compute the cosin between two inputs, but use h_vec as the base vector

import math

r_trans="live_result.txt" #recognized transcription
h_trans="Andy_tran7.txt" #human labeled transcription
sas_tfile="sastlist_rmTalk3000.txt" #sas terminology file, typically filtered by en_stopwords and talk3000 words

#use a dict to store sas teminology term
sas_term_dict={}

sas_read_tfile=open(sas_tfile)
sas_term_ct=sas_read_tfile.readlines()
sas_read_tfile.close()

for line in sas_term_ct:
    line_0=line.strip()
    sas_term_dict[line_0]=1

#filter the recognized transcription
r_file=open(r_trans)
r_ct=r_file.readlines() #in fact only one line...
r_file.close()

r_dict={}

for line in r_ct:
    line_0=line.strip() #not one line !
    line_1=line_0.split(' ')
    for word in line_1:
        if sas_term_dict.get(word)==1: #current word is in the sas terminology
            if r_dict.get(word)==None: #haven't been stored before
                r_dict[word]=1
            else:
                r_dict[word]=r_dict[word]+1

#filter the human labeled transcription
h_file=open(h_trans)
h_ct=h_file.readlines() #in fact only one line...
h_file.close()

h_dict={}

for line in h_ct:
    line_0=line.strip() #in fact one line
    line_1=line_0.split(' ')
    for word in line_1:
        if sas_term_dict.get(word)==1: #current word is in the sas terminology
            if h_dict.get(word)==None: #haven't been stored before
                h_dict[word]=1
            else:
                h_dict[word]=h_dict[word]+1

#use the longer dict as the base vector

r_vec=[]
h_vec=[]

if len(h_dict.keys()) > len(r_dict.keys()):
    for word in h_dict.keys():
        h_vec.append(h_dict.get(word))
        if r_dict.get(word)==None:
            r_vec.append(0)
        else:
            r_vec.append(r_dict.get(word))
else:
    for word in r_dict.keys():
        r_vec.append(r_dict.get(word))
        if h_dict.get(word)==None:
            h_vec.append(0)
        else:
            h_vec.append(h_dict.get(word))

# Input: 2 vectors
# Output: the cosine similarity
# !!! Untested !!!
def cosine_similarity(vector1,vector2):
    # Calculate numerator of cosine similarity
    sumdot=0.0
    for i in range(len(vector1)):
        sumdot=sumdot+(vector1[i]*vector2[i])
    # Normalize the first vector
    sum_vector1 = 0.0
    for i in range(len(vector1)):
        sum_vector1=sum_vector1+(vector1[i]*vector1[i])
    norm_vector1 = math.sqrt(sum_vector1)
    # Normalize the second vector
    sum_vector2 = 0.0
    for i in range(len(vector2)):
        sum_vector2=sum_vector2+(vector2[i]*vector2[i])
    norm_vector2 = math.sqrt(sum_vector2)
    return (sumdot/(norm_vector1*norm_vector2))

print "the cosin distance is "+str(cosine_similarity(h_vec, r_vec))+'\n'

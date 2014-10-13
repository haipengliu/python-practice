
# This script reads in two inputs, transcribed text and {word-id : time(sec)}
# mapped file.
# Output a file contains {word-char : occuring time (sec)} information
# TAG haipeng

import os
import sys

path='/kaldi/kaldi-trunk/egs/voxforge/online_demo/'
model_type=path+'online-data/models/tri3b_adapted_mmi/'
fn_trans=sys.argv[1] #input live_result.txt
fn_stime_out=sys.argv[2] #input word_id_second.txt(output_stime.txt)

dict_word_id={} # {word-char : pos-id} 
fr_trans=open(fn_trans)
ct_trans=fr_trans.readlines()
fr_trans.close()

gb_pos=1 #global word pos id

for line0 in ct_trans:
    line1=line0.strip()
    line2=line1.split(' ')
    for word0 in line2:
        word1=word0.strip()
        if word1 != "":
            dict_word_id[gb_pos]=word1
            gb_pos=gb_pos+1
            
# check code
#f_test=open('word_pos_test.txt','w')
#for i in range(len(dict_word_id)):
#    f_test.write(dict_word_id.get(i+1)+' '+str(i)+' ;')
   
dict_pos_sec={} # {word-pos : time-sec} 
fr_stime_out=open(fn_stime_out) 
ct_stime_out=fr_stime_out.readlines()
fr_stime_out.close()

for line0 in ct_stime_out:
    line1=line0.strip()
    line2=line1.split(' ')
    if len(line2)==2:
        dict_pos_sec[line2[0]]==line2[1]
    else:
        print "Split word-pos : time-sec file line error "




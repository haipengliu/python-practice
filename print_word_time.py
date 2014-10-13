import os
import sys
#This script will read the output file from prons-to-word.cc in Kaldi
#It will read the word.txt, convert the word-id and frame-length to
#a readable form => word (start-time, end-time(in second))
#TAG Haipeng

path='/kaldi/kaldi-trunk/egs/voxforge/online_demo/'
#model_type=path+'online-data/models/tri3b_adapted_mmi/'
model_type=path+'online-data/models/tri2a_GPU/'
fn_word_time=sys.argv[1] #input 'wdali.txt'
fn_stime_out=sys.argv[2] #output stime.txt

f_word_int=open(model_type+'words.txt')
ct_word_int=f_word_int.readlines()
f_word_int.close()
#Use a dict to store word-int, and transfer word-id to word-char
dict_int_word={}

for line in ct_word_int:
    line0=line.strip()
    line1=line0.split(' ')
    dict_int_word[line1[1]]=line1[0]

#Open the word-time-alignment file
f_word_time=open(path+fn_word_time)
ct_word_time=f_word_time.readlines()
f_word_time.close()

dict_utt_dict3bros={} #each utt mapped to a dict of list of 3 bros (char, st-time,ed-time) indexed by pos

###############################################################################
# dict_utt_pos_word_time is a dictionary map a utterance id to a 3 items list#
# The 3 items list contains [word char, start time, end time]  #
###############################################################################

utt_name_list=[]
#Try to get the total frames
frame_total=0



for line in ct_word_time:
    line0=line.strip()
    line1=line0.split(' ',1)
    utt_id=line1[0] #utterance id
    utt_name_list.append(utt_id)
    dict3bros={} #dict_utt_dict3bros[utt_id]=dict3bros,dict3bros[pos]=[word_char,st_time,ed_time]
    ct_uttid=utt_id.split('_')
    utt_length=ct_uttid[-1] #frames: 0-1404
    utt_fn_name=ct_uttid[0:(len(ct_uttid)-2)]
    len_tmp=utt_length.split('-')
    if len(len_tmp)!=2:
        print >> sys.stderr,"frame start-to-end indicator not equals two\n"
        break
    else:
        if int(len_tmp[-1])>frame_total:
            frame_total=int(len_tmp[-1])
        utt_st_fr=int(len_tmp[0]) #utterance start frame id
        utt_ed_fr=int(len_tmp[1]) #utterance end frame id
        word_frlen=line1[1].split(';')
        for i in range (len(word_frlen)):
            wd_fl=word_frlen[i].strip()
            wd_fl0=wd_fl.split(' ')
            if len(wd_fl0)!=2:
                print >> sys.stderr,"word-id frame-length pair split error\n"
                break
            else: #3 brothers
                word_pos=i #will be the index in the 3-brothers dict
                word_id=wd_fl0[0] 
                frm_len=int(wd_fl0[1]) #will be transformed to start-time#1 and end-time#2
                word_char=dict_int_word[word_id] #transform to word#0
                if word_pos==0:
                    start_frm=utt_st_fr #start frame
                    end_frm=start_frm+frm_len #end frame, is -1 correct??
                    three_bros_tmp=[]
                    three_bros_tmp.append(word_char)
                    three_bros_tmp.append(start_frm)
                    three_bros_tmp.append(end_frm)
                    dict3bros[word_pos]=three_bros_tmp
                else:
                    start_frm=(dict3bros.get(word_pos-1))[2]+1
                    end_frm=start_frm+frm_len-1
                    three_bros_tmp=[]
                    three_bros_tmp.append(word_char)
                    three_bros_tmp.append(start_frm)
                    three_bros_tmp.append(end_frm)
                    dict3bros[word_pos]=three_bros_tmp
    dict_utt_dict3bros[utt_id]=dict3bros
    
        
#1 frame = 10ms, 1s=1000ms, total wav length
wav_len=(frame_total*10)/1000

# f_output=open('word_time_test.txt','w')

# for x in utt_name_list:
#     tail=dict_utt_dict3bros[x]
#     for i in range(len(tail)):
#         #f_output.write(str(i)+' '+tail.get(i)[0]+' '+str(tail.get(i)[1])+' '+str(tail.get(i)[2])+'; ')
#         f_output.write(str(i)+' '+tail.get(i)[0]+' '+str(((tail.get(i)[1])*10)/1000)+' '+str(((tail.get(i)[2])*10)/1000)+'; ')
#     f_output.write('\n')
    
# f_output.write(str(wav_len)+'\n')
# f_output.close()

############################################################################
#Transform the content in dict_utt_dict3bros into a compact dict which could
#be read by the index-processer of IRstudio in the following form:
#global postion'\t'start-second
#1		0
#2		0
#3		0
#4		0
#6		1
#
#44		12
#45...
#
#these content will be put into a new field in IRstudio named 'stime'#
############################################################################

gb_pos=0 #global postion
ir_index={} # dict containing word_pos'\t'start_time for index server of IR
#It map a global word position (in document) to a [word_char, start-second]

for utt in utt_name_list:
    tail=dict_utt_dict3bros[utt] #utt-id : utt-sentence(tail)
    for i in range(len(tail)):
        if tail.get(i)[0]!='<eps>':
            gb_pos=gb_pos+1
            list_tmp=[]
            list_tmp.append(tail.get(i)[0]) #word-char
            start_second=((tail.get(i)[1])*10)/1000 #time-sec
            list_tmp.append(start_second)
            ir_index[gb_pos]=list_tmp

f_ir_index=open(path+fn_stime_out,'w')

for i in range(len(ir_index)):
    f_ir_index.write(ir_index.get(i+1)[0]+'\t'+str(ir_index.get(i+1)[1])+'\n')

f_ir_index.close()



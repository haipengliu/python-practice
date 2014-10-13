import os

dir0 = '//kaldi//sas-podcast-processed//'
dir1 = '//kaldi//trans//'
dir2 = '//kaldi//wav//'
dir3 = '//kaldi//trans-spk-named//'
dir4 = '//kaldi//wav-spk-named//'
txtfile=[]
wavfile=[]
txtname='.txt'
wavname='.wav'


#split txt files and wav files into two lists txtfile and wavfile
for root, dirs, files in os.walk(dir0):
    for f in files:
        name=f[-4:-1]+f[-1]
        if (name == txtname):
            txtfile.append(f)
        elif (name == wavname):
            wavfile.append(f)

print str(len(txtfile))+'\t'+str(len(wavfile))

txtfiletmp=[]
wavfiletmp=[]


#remove suffix .txt and store just file name into txtfiletmp
for x in txtfile:
    #print x[0:-4]
    txtfiletmp.append(x[0:-4])

#remove suffix .wav and store just file name into txtfiletmp
for x in wavfile:
    wavfiletmp.append(x[0:-4])

for x in txtfiletmp:
    if x not in wavfiletmp:
        print 'the file '+x+'.txt is not included in the wavfiletmp list!'

        
if len(txtfiletmp) == len(wavfiletmp):
    print 'File alignment OK!\n'
else:
    print '.txt files and .wav files not alignment!'

#remove the addtional '\n' and write them into 'trans'    
#for x in txtfile:
#    filename = dir0+x
#    fi= open(filename)
#    ct = fi.readlines()
#    fi.close()
#    wfilename = dir1+x
#    fw = open(wfilename,'w')
#    for line in ct:
#        tline = line.strip()
#        fw.write(tline)
#    fw.close()

    
#use the last word (lecture's name) to rename the file
#write the renamed file into /trans
def rename_trans_wav(filenamelist):
    #filenamelist = txtfiletmp
    for x in filenamelist:
        filename1=dir3+x+'.txt'
        filename2=dir4+x+'.wav'
        fi=open(filename1)
        ct=fi.readlines()
        fi.close()
        # Only one paragraph in speech
        if (len(ct)>1) or (len(ct)==0): 
            print 'file '+x+' length error!'
        elif len(ct)==1:
            line = ct[0].strip()
            words = line.split(' ')
            speaker = words[-1]
            if speaker[0].islower():
                print 'The spk name still error '+speaker+'\t'+x+'.txt\n'
            else:
                wfilename1=dir3+speaker+'-'+x+'.txt'
                wfilename2=dir4+speaker+'-'+x+'.wav'
                os.rename(filename1, wfilename1)
                os.rename(filename2, wfilename2)
    
#remove the last speaker's name in the transcription
def upper_remove_spk(dir_path_in,dir_path_out):
    #trans_spk_files = os.listdir(dir_path_in) 
    for fn in os.listdir(dir_path_in):
        #print fn
        fi = open(dir_path_in+fn)
        ct = fi.readlines()
        fi.close()
        fnline = fn.split('-')
        spk=fnline[0]
        line = ct[0].strip()
        #print spk+'\n'
        words = line.split(' ')
        #print words[-1]+'\n'
        if words[-1] != spk :
            print 'speak\'s name do not match file\'s name\n'
        else:
            fo = open(dir_path_out+fn,'w')
            for word in words[0:len(words)-1]:
                fo.write(word.upper()+' ')
            fo.close()


            
#rename_trans_wav(txtfiletmp)
#a = '//kaldi//trans-spk-named//'
#b = '//kaldi//trans-spk-named2//'
#upper_remove_spk(a,b)

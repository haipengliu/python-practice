#!usr/bin/python

# this python script is to emerge the WER results computed by compute_exp_wer.sh
# It open each exp_wer_* file in wer_stat folder, and then compute the mean value of the WER for each exp step
# by TAG BRD haipeng liu

import os
import sys
import re
from operator import itemgetter

path = r'/kaldi/kaldi-trunk/egs/voxforge/s8_2014_02_10_voxforge_GPU_support/wer_stat'

def WalkDir(dir):
    flist = []
    new_flist = []
    for root, dirs, files in os.walk(dir):
        for f in files:
            #fn = root+'/'+f
            #print fn
            #if file_callback: file_callback(f, fn)
            flist.append(f)
        sp_flist = split_list_element(flist)
        sp_flist.sort(elem_cmp)
        newsp_flist = reshape_name(sp_flist)
        #for x in newsp_flist:
        #    print x
        
    return newsp_flist

def split_list_element(flist):
    sp_flist = []
    for fn in flist:
        st_fn = fn.strip()
        sp_fn = re.split('[_:]', st_fn)
        if len(sp_fn) > 1:
            sp_fn[1] = int(sp_fn[1])
            sp_fn[2] = int(sp_fn[2])
            sp_fn[3] = int(sp_fn[3])
            sp_flist.append(sp_fn)
    return sp_flist

def elem_cmp(ls1, ls2):
    if ls1[1] != ls2[1]:
        return cmp(ls1[1], ls2[1])
    elif ls1[2] != ls2[2]:
        return cmp(ls1[2], ls2[2])
    elif ls1[3] != ls2[3]:
        return cmp(ls1[3], ls2[3])
    else:
        return cmp(ls1[3], ls2[3])

def reshape_name(fnlists):
    new_fnlists = []
    for fnlist in fnlists:
        for x in [1, 2, 3]:
            fnlist[x] = str(fnlist[x])
            if len(fnlist[x]) == 1:
                fnlist[x] = '0' + fnlist[x]
        new_fn = fnlist[2] + ':' + fnlist[3]
        fnlist[2] = new_fn
        del fnlist[3]
        new_fnlists.append('_'.join(fnlist))
    return new_fnlists
            


def compute_mean_wer(fnlist, path):
    """open the exp_wer_* file and compute&write the mean wer into the 'wfn' file
    
    :type fnlist: list
    :param fnlist: the list contains exp_wer file name, sorted in time order

    :type path: string
    :param path: the exp_wer file name with the full path
    
    """
    for fn in fnlist:
        try:
            fd = open(path+'/'+fn)
            content = fd.readlines()
            fd.close()
            print "processing " + path + '/' + fn
            i = 0
            sum = 0.0
            for line in content:
                st_line = line.strip()
                if "%WER" in st_line:
                    i = i + 1
                    sp_line = re.split('[ +]',st_line)
                    wer_val = sp_line[1]
                    sum += float(wer_val)
            if i == 0 and sum == 0:
                pass
            else:
                mean_wer = sum/i
                fdout.write(fn + ': mean WER% is '+ str(mean_wer)+'\n')
        except:
            print >> sys.stderr,"Error open" + path + '/' + fn 

fdout = open(r'wer_stats.txt', 'w')

flist = WalkDir(path)
compute_mean_wer(flist, path)

fdout.close()




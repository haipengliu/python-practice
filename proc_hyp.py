#!usr/bin/python

# this script is to fix the decoded result hyp.txt
# when decoding the long WAV file such as podcast.
# the original successive alignments could be seperated into different segments.
# we need to re-join those segments back to the original one
# by TAG BRD haipeng liu

import os
import sys
import re

class term_frame_trans():
    def _init_(self):
        self.frame = 0
        self.trans = ""
    
def frm_cmp(tft1, tft2):
    return cmp(tft1.frame, tft2.frame)


def find_wav_list(content):
    wav_list = []
    for line in content:
        strline = line.strip()
        spline = strline.split(' ')
        fn = spline[0]
        wav_list.append(fn)
    return wav_list

def find_trans_dict(content):
    trans_dict = {}
    for line in content:
        strline = line.strip()
        reline = re.sub(' +', ' ', strline)
        spline = reline.split(' ')
        fn = spline[0] # fn with the frame info suffix
        trans_list = spline[1:len(spline)]
        (new_fn, frm1) = make_newfn(fn) # fn without the frame info suffix
        new_trans = make_newtrans(trans_list)
        frame_trans = term_frame_trans()
        frame_trans.frame = frm1
        frame_trans.trans = new_trans
        if trans_dict.has_key(new_fn) == False:
            new_obj_list = []
            new_obj_list.append(frame_trans)
            #print len(new_obj_list)
            #print 'new_fn:'+new_fn+' frame:'+str(new_obj_list[0].frame)+' trans:'+new_obj_list[0].trans
            trans_dict[new_fn] = new_obj_list
            #print "new_obj_list:"+trans_dict.get(new_fn)
        else:
            obj_list = trans_dict.get(new_fn)
            obj_list.append(frame_trans)
            trans_dict[new_fn] = obj_list
            #print len(trans_dict.get(new_fn))
    return trans_dict

def make_newfn(fn):
    spfn = fn.split('_')
    fn_list = spfn[0:len(spfn)-1]
    frm_info = spfn[len(spfn)-1]
    sp_frminfo = frm_info.split('-')
    frm1 = int(sp_frminfo[0])
    new_fn = ""
    for fn_piece in fn_list:
        if new_fn == "":
            new_fn = fn_piece
        else:
            new_fn = new_fn+'_'+fn_piece
    return (new_fn, frm1)


def make_newtrans(trans_list):
    new_trans = ""
    for trans_term in trans_list:
        if new_trans == "":
            new_trans = trans_term
        else:
            new_trans = new_trans+' '+trans_term
    return new_trans

def validate(wav_list, trans_dict):
    if len(wav_list) == len(trans_dict):
        print "The number of utterances in fixed hyp file matches the wav file number in input.scp."
        return;
    else:
        print "proc_hyp.py error.\nThe number of utterances in fixed hyp file does not match the wav file number in input.scp\n "
        sys.exit(1)

def remove_sorted_frm_info(trans_dict):
    new_dict ={}
    for wav in trans_dict.keys():
        obj_list = trans_dict.get(wav)
        trans = ""
        for obj in obj_list:
            if trans == "":
                trans = obj.trans;
            else:
                trans = trans + ' '+ obj.trans;
        new_dict[wav] = trans
    return new_dict

def write_new_hyp(trans_dict, fd_newhyp):
    for (k, v) in trans_dict.items():
        fd_newhyp.write(k + ' ' + v + '\n')
    return

def pre_process(argument):
    if len(sys.argv) != 3:
        print "usage: python proc_hyp.py <input-directroy> <output_file>\ne.g. python work work/new_hyp.txt\n"
        sys.exit(1)
    else:
        try:
            fd_scp = open(sys.argv[1]+'/input.scp')
        except:
            print >> sys.stderr, "Error open "+sys.argv[1]+" /input.scp\n"
        try:
            fd_hyp = open(sys.argv[1]+'/hyp.txt')
        except:
            print >> sys.stderr, "Error open "+sys.argv[1]+" /hyp.txt\n"
        ct_scp = fd_scp.readlines()
        ct_hyp = fd_hyp.readlines()
        fd_scp.close()
        fd_hyp.close()
        wav_list = find_wav_list(ct_scp)
        trans_dict = find_trans_dict(ct_hyp)
        # to do
        validate(wav_list, trans_dict)
        for wav in trans_dict.keys():
            #print "Now printing the DICT:\n"
            #print "wav name :"+wav
            frame_trans_list = trans_dict.get(wav)
            #for x in frame_trans_list:
            #    print x.frame
            frame_trans_list.sort(frm_cmp)
            #for frame_trans_class in frame_trans_list:
            #    print frame_trans_class.frame
            trans_dict[wav] = frame_trans_list

        sort_trans_dict = remove_sorted_frm_info(trans_dict)
        fd_newhyp = open(sys.argv[2],'w')
        write_new_hyp(sort_trans_dict, fd_newhyp)
        fd_newhyp.close()
        print "Finish fixing the hyp file."
        return


pre_process(sys.argv)


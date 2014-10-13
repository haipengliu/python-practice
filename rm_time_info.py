#!usr/bin/python

# this python script receive a string with the time info and the file name. 
# then it remove the time info and return the clean file name
# by TAG BRD haipeng liu

import sys

time_info = sys.argv[1]
st_tinfo = time_info.strip()
sp_tinfo = st_tinfo.split('_')

true_fn = ""

for x in sp_tinfo[3:len(sp_tinfo)]:
    if x == sp_tinfo[3]:
        true_fn = x
    else:
        true_fn = true_fn + '_' + x

print true_fn

#!usr/bin/python

# this python script receives a string from shell command 'ls -lt exp/'
# then it find the time info and join it with the file name
# by TAG BRD haipeng liu

import sys
import re

ls_info = sys.argv[1]

st_lsinfo = ls_info.strip()
re_lsinfo = re.sub(" +", " ", st_lsinfo)
sp_lsinfo = st_lsinfo.split(" ")

idx = len(sp_lsinfo)


if len(sp_lsinfo) != 2:
    add_time_info = sp_lsinfo[idx-4]+'_'+sp_lsinfo[idx-3]+'_'+sp_lsinfo[idx-2]+'_'+sp_lsinfo[idx-1]
    print add_time_info



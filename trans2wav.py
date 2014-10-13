#!/usr/bin/python -u

import sys
import os
import os.path

from optparse import OptionParser

# SAS Institue Speech2Text Demo
# TAG BRD by Haipeng Liu
# This script can be used to transform the video/audio file in the input directory into the WAV file format
# The transformed files can be placed in the output directory. If the output directory does not exist, this command will create one.

parser = OptionParser()
parser.add_option('--input', dest='input',help="the input directory where you puts the video/audio files in")
parser.add_option('--output', dest='output',help="the output directory storing the transformed WAV files")

(options, args) = parser.parse_args()

if(options.input in [None, ""] or options.output in [None, ""]):
    parser.print_help()
    sys.exit(1)

input = os.path.dirname(options.input)
output = os.path.dirname(options.output)

print input

if not os.path.exists(input):
    print "input directory "+input+" not exits."
    sys.exit(1)

if not os.path.exists(output):
    os.makedirs(output)

sox_format = ['wav', 'flac', 'avi', 'wmv', 'mp2', 'mp3', 'mp4', 'vox', 'pcm']

for root, dirs, files in os.walk(input):
    for f in files:
        fn_suffix = f.split('.')
        print fn_suffix
        #if fn_suffix[-1] in sox_format:
        #    os.system('sox '+f+' -b 16 -s -c 1 -r 16k '+output+'/'+fn_suffix[0:-2]+'.wav')

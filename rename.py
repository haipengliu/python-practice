import os

path = 'E:\\OpenSource\\Sphinx\\SAS777\\'
wav_file = []
rootdir = os.listdir(path)
x = 'wav'


for filename in rootdir:
	if x in filename:
		wav_file.append(filename)

wav_changed = []
		
if len(wav_file) == 172 :
	for n in wav_file :
		m = n.strip()
		a = m.split('_')
		b = a[1].split('.')
		c = int(b[0])+605
		d = 'arctic_0'+str(c)+'.wav'
		os.rename(m,d)

else:
	print 'wav file read error, not the correct number.\n'

	
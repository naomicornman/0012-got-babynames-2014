from os.path import basename, join
import string
import requests

DATADIR = 'tempdata'

URL = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
babypath = join(DATADIR, basename(URL))
babyfile = open(babypath, 'r')

m_dict = {}
f_dict = {}
# ...etc

l = 'letter'
f = 'F'
m = 'M'

print (l, f.rjust(9), m.rjust(7)) 
print ('-'*24)

with open(babypath) as f:
	for line in f:
		name, sex, babies = line.strip().split(',')
		if sex == 'F':
			last_letter = name[-1]
			if f_dict.get(last_letter):
				f_dict[last_letter] += int(babies)
			else: 
				f_dict[last_letter] = int(babies)

with open(babypath) as f:
	for line in f:
		name, sex, babies = line.strip().split(',')
		if sex == 'M':
			last_letter = name[-1]
			if m_dict.get(last_letter):
				m_dict[last_letter] += int(babies)
			else: 
				m_dict[last_letter] = int(babies)
 		

letters = string.ascii_lowercase
for key in letters:
	fval = str(f_dict[key])
	mval = str(m_dict[key])
	print (key, fval.rjust(14), mval.rjust(7))

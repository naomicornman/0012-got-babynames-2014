import requests
from os.path import basename, join

DATADIR = 'tempdata'

URL = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
babypath = join(DATADIR, basename(URL))

d = 0 

with open(babypath) as f:
	for line in f:
		name, sex, babies = line.strip().split(',')
		if name == 'Daenerys':
			d += int(babies)

print ('Daenerys', d)

k = 0
with open(babypath) as f:
	for line in f:
		name, sex, babies = line.strip().split(',')
		if 'Khalees' in name or 'Khaless' in name:
			k += int(babies)

print ('Khaleesi', k)

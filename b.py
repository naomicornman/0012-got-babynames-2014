from os.path import basename, join

DATADIR = 'tempdata'

URL = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
babypath = join(DATADIR, basename(URL))

totalbabies = 0
with open(babypath) as f:
	for line in f:
		totalbabies += int(line.split(',')[2])

print("There are", totalbabies, 'whose name were recorded in 2014')

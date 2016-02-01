from os.path import basename, join

DATADIR = 'tempdata'

URL = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
babypath = join(DATADIR, basename(URL))

fx = 0
mx = 0

with open(babypath) as f:
	for line in f:
		name, sex, babies = line.strip().split(',')
		if sex == 'F':
			fx += int(babies)

with open(babypath) as f:
	for line in f:
		name, sex, babies = line.strip().split(',')
		if sex == 'M':
			mx += int(babies)

print("F:", fx)
print("M:", mx)

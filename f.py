from os.path import join
import string
import requests
DATADIR = 'tempdata'
babypath = join(DATADIR, 'ssa-babynames-nationwide-2014.txt')
babyfile = open(babypath, 'r')

mydict = {}

for line in babyfile:
	name, sex, babies = line.strip().split(',')
	last_letter = name[-1]
	
	if mydict.get(last_letter):
		mydict[last_letter] += int(babies)
	else:
		mydict[last_letter] = int(babies)
		
		
letters = string.ascii_lowercase
for letter in letters:
     val = mydict[letter]
     print (letter, ':', val)

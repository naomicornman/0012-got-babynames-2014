
import os
babypath = os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')
babyfile = open(babypath, 'r')

print ("Top baby girl names")


with open(babypath) as f:
	lines = f.readlines()
	counter = 1
	for line in lines[0:5]:
		topbabynames = (line.split(',')[0])
		topbabynum = (line.split(',')[2])
		print (counter, ".", topbabynames,topbabynum)
		counter = counter + 1



print ("Top baby boy names")

with open(babypath) as f:
	lines = f.readlines()
	counter = 1
	for line in lines[19068:19073]:
		topbabynames = (line.split(',')[0])
		topbabynum = (line.split(',')[2])
		print (counter, ".", topbabynames,topbabynum)
		counter = counter + 1

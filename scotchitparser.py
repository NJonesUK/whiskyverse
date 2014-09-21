import csv

scotchitfile = open("scotchit-linksremoved.csv", 'r')
whiskynamefile = open("whiskynames.txt", 'w')

whiskylist = []

scotchitreader = csv.reader(scotchitfile)
for line in scotchitreader:
	if line[0] in whiskylist:
		pass
	else:
		whiskylist.append(line[0])
		whiskynamefile.write(line[0] + '\n')


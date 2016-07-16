'''
A simple Program for Coursera. Python Data Structure $Chapter 8

Open and read a file line by line, then find lines start with "From". 
(eg: From stephen.marquar@ut.ac.za Sat Jan ...) Parse the line using split
then print out the e-mail address. At last, print the amount of addresses.

Author: Lynn Lau
Date: 2016/07/16
Version: 1.0
'''
path = "D:mbox-short.txt"
file = open(path)
List = []
AddressList = []
i = 0
#CountLine = 0
for line in file:
	if line.startswith('From:'):
		Line = line.split()
		List.append(Line)
		#CountLine = CountLine + 1
while i < len(List):
	AddressList.append(List[i][1])
	i  = i + 1
for item in AddressList:
	print item
#print AddressList
print 'There were %d lines in the file with From as the first word' % len(List)	


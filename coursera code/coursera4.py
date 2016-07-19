'''
A Simple Program for Coursera  Python Data Structures $ Chapter turple

Write a program to read through the mbox-short.txt and figure out 
the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the 
time and then splitting the string a second time using a colon.
i.e. 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
Once you have accumulated the counts for each hour, 
print out the counts, sorted by hour as shown below.

Author: Lynn Lau
Date: 2016/07/19
Version: 1.0
'''
path = 'D:mbox-short.txt'
file = open(path)
#lines = file.readline()
#print lines
# Choose the right lines and split the words,
# then add them into a list
timeList = list()
hourDict = dict()
for line in file:
	if line.startswith('From'):
		Line1 = line.split()
		if len(Line1) > 2:
			timeList.append(Line1[5].split(':')[0])
			#print Line1[5].split(':')	
            #print type(Line1[5])
		else:
			continue
		#print Line
#print timeList
# Initalize a dictionary and make a counter 
# count the requency of the words
for hour in timeList:
	hourDict[hour] = hourDict.get(hour,0) + 1
#print hourDict
# Sort the turples and print them
sortedList = list()
for (key,val) in hourDict.items():
	sortedList.append((key,val))
sortedList.sort()
#print sortedList
for k,v in sortedList:
	print k,v
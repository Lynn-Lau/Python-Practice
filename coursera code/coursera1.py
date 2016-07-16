'''
A Simple Program for Coursera Python Data Structure $ Chapter 8 List

Open a file and read the file line by line.Split the line into words
and print them.May be some words shoud be split twice.

Author: Lynn-Lau
Origin Date: 2016/07/14 Version: 1.0 
Modified Date: 2016/07/16 Version: 1.1
'''
path = 'D:romeo.txt'
List = []
sortedList = []
CountLine = 0
file = open(path)
for line in file:
	Line = line.split()
	for item in Line:
		List.append(item)	
	CountLine = CountLine + 1
SortedList = List.sort()
for item in List:
    if item not in sortedList:
        sortedList.append(item)

print sortedList
 
#print CountLine
#print SetList
'''
line = file.read().split('\n')
Line0 = line[0].split()
for item in Line0:
	List.append(item)

print List
'''
'''
List = line[0].split() + line[1].split() + line[2].split()
List1 = List.append('who')
SortedList = List.sort()
print
''' 

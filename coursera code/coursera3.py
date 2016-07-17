'''
A Simple Program for Coursera. Python Data Structure Chapter $9 Dictionary

Read the file 'mbox-short.txt' figure out who sent the most great number
of e-mails, then print it out.

Author: Lynn Lau
Date: 2016/0717
Version: 1.0
'''
path = 'D:mbox-short.txt'
file = open(path)
List = list()
AddressList = list()

for line in file:
	if line.startswith('From:'):
		Line = line.split()
		List.append(Line)
#print List

index = 0
while index < len(List):
	AddressList.append(List[index][1])
	index = index + 1
	#pass
#print AddressList

counts = dict()
for address in AddressList:
	counts[address] = counts.get(address,0) + 1 
	#pass
#print counts

bigCount = None
bigAddress = None
for address,count in counts.items():
	if bigCount is None or count > bigCount:
		bigCount = count
		bigAddress = address

print bigAddress, bigCount
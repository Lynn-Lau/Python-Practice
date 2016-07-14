'''
A Simple Program for Coursera Python Data Structure $ Chapter Seven  Files

Open a file whose name is "mbox-short.txt"
Look for lines just like "X-DSPAM-Confidence : 0.8475"
Count the lines of them and Calculate the AVERAGE Value of float numbers 

Author:Lynn-Lau
Date: 2016/07/14
Version: 1.1

READEME
1 Updated the method of how to calculate the Value and Average Value
2 Canceled the lambda function
'''
path = 'D:\mbox-short.txt'
file = open(path,'r')
NumberList = []
for line in file:
	Line = line.strip()
	if Line.startswith('X-DSPAM-Confidence:'):
		Number = float(Line[20:])
		NumberList.append(Number)

Index = 0
Value = 0
while Index < len(NumberList):
	Value = Value + NumberList[Index]
	Index = Index + 1

AverageValue = Value/len(NumberList)
print "Average spam confidence: %.12f" % AverageValue
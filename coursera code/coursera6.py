"""
A simple program for Coursera Python $ Loop

Promot users input some numbers and make a comparation,
out put the largest and smallest number.

Author: Lynn Lau
Date: 2016/07/21
Version: 1.0
"""
largest = None
smallest = None
numberList = list()

while True:
	num = raw_input("Enter a number: ")
	if num == "done":
		print "Invalid input"
		break
	try:
	    numberList.append(int(num))
	except:
		print "Invalid input"
#print numberList
for value1 in numberList:
	if largest is None:
		largest = value1
	elif value1 > largest:
		largest = value1
		

for value2 in numberList:
	if smallest is None:
		smallest = value2
	elif value2 < smallest:
		smallest = value2
		 
print "Maximum is", largest
print "Minimum is", smallest 
'''
A Simple Program for Coursera Python Data Structure $ Chapter 8 List

Open a file and read the file line by line.Split the line into words
and print them.May be some words shoud be split twice.

Author: Lynn-Lau
Version: 1.0  
'''
path = 'D:romeo.txt'
file = open(path)
line = file.read().split('\n')
List0 = line[0].split()
List1 = line[1].split()
List2 = line[2].split()
List = List0 + List1 + List2
print List
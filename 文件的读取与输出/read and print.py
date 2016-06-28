#-*- coding:utf-8 -*-

path = ("E:\split\part0001.txt")

file = open(path)
L = [line.split() for line in open(path)]
# print len(L)
File = open("test.txt",'w')

num = 0
while num < len(L):
    print L[num][4]
    File.write(L[num][4])
    num += 1

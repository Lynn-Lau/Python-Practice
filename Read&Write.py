##############################
# 此次练习读取txt文档并将读取的内容添加到list中
# 然后写入另一个txt文件之中
##############################

# Author: Lynn-Lau
# Language: Python 2.7

// 首先声明一个空的列表ContentList
ContentList = []
// 打开文件
with open('filename') as file:
    for line in file:
	    // 按照默认的字符串解析方式解析之后添加
		// 到ContentList
	    ContentList.append(line.split())

// 以可写的方式打开新文件		
NewFile = ('newfile.txt','w')
// 用迭代的方法将ContentList 中的内容添加
// 前提是将list中内容转化为字符串格式
for LineContent in ContentList:
    NewFile.write(str(LineContent))
// 关闭文件	
NewFile.close()
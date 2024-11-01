import csv#we are import csv library because we are reading file like a excel file here
with open('d.txt')as file:
    List=csv.reader(file)#it will store the data like lists
    for currow in List:
        print(currow)
        # print(', '.join(currow)) by using .join() we can format the way we want to print output
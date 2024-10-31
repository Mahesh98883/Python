#list is a object in python to store multiplevalues
scores=[3,5,2,5,2,7,6]
scores.append(4)#append is used to add an extra value to current lsit
scores.remove(5)#remove vlaue from list
#we can also use del scores[index of number you want to delete]
#if there are multiple occurences of values it will delete first one
scores[4]=3#update a value in index num4
print(scores)
print(scores[-1])#prints last value of list
#searching list
print(scores.index(5))
n=len(scores)#len is used to find the length of lists
for i in range(n):
    print(scores[i])
scores.sort()
for score in scores:
    print(score)
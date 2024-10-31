guests=[]
name=""
while name!="exit":
    name=input("Enter the guests name(enter exit if no more names)): ")
    guests.append(name)
guests.sort()
guests.remove('exit')
for guest in guests:
    print(guest)
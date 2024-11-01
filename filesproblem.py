import csv
with open('guests.txt') as file:
    list=csv.reader(file)
    for guestslists in list:
        print(guestslists)

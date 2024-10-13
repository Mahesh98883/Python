a=int(input("what is your kd?"))
season=int(input('from which season you are palying'))
if a==1:#if it satisfies 1st condition it won't run another conditions below
    print("Noob")
elif a==2:#elif is shortform of elseif
    print("good")

elif a>4 and season==18 or season==19:#we can combine and,or to if statements here 'and' is evaluated first
    print("ultrapromax")
elif a>3 or season==18:#if either of one condition holds true it will print the below desired output
    print("pro")
elif a>3 and season==18:#here two conditions must be hold true for below desired output
     print('ultra pro')

else:
    print("hatt ja")

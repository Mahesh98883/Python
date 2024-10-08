a=int(input("salary: "))# a is a variable name and we are giving user input as integer using int
b=input("are u a govt employee: ")#bydefault it will take user input as string
if(a>30000):#checking if salary is greater than 30000
   

    if(b=='yes'):#we use == to comapre values in python in if else condition
        print("No tax will be deducted")#if user input is YES then if condition is not satisfied because python is case sensitive
        
    else:#if answer is not yes then else will be executed
        print("Tax of 15% will be deducted")
        if(a>100000):
            extratax=True
        if extratax:
            print("pay extra tax")

print(a)
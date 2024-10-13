# Calculate shipping charges for a shopper

# * Ask the user to enter the amount for their total purchase

# If their total is under $50 add $10, otherwise shipping is free

# Tell the user their final total including shipping costs and forma the number so it looks like a monetary value

# Don't forget to test your solution with

# -a value 50

# - a value 50

# -a value of exactly 50
ShippingCharges=int(input())
b=ShippingCharges+10
if(ShippingCharges<50):
    print("extra $10 need to be paid for shipping under $50")
    print("$"+str(b)+"only")#using str(b) for converting int to str for printing output with dollar symbol
else:
    print("$"+str(ShippingCharges)+"only")


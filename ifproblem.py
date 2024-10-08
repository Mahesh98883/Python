ShippingCharges=int(input())
b=ShippingCharges+10
if(ShippingCharges<50):
    print("extra $10 need to be paid for shipping under $50")
    print("$"+str(b)+"only")
else:
    print("$"+str(ShippingCharges)+"only")


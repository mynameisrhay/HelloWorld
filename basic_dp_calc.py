# 3rd exercise. basic down payment calculator based on whether the payer has good credit or not. basic if functions
# if buyer has good credit, they only need to down 10%. If not, 20%

house_price = 1000000
buyer_gc = input("Does this payer has good credit? (Y/N) ")

if buyer_gc.upper() == "Y":
    print(f"Your required down payment is {house_price * .10}")
elif buyer_gc.upper() == "N":
    print(f"Your required down payment is {house_price * .20}")
else:
    print("Make sure you filled the good credit status correctly")

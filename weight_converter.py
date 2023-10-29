# 2nd exercise. simple weight converter from lbs to kgs vice versa. this won't use the IF function

weight = float(input("What is your weight? "))
weight_unit = input("Is it in (K)gs or (L)bs? ")

if weight_unit.upper() == "K":
    print(f"Your weight in Lbs is {weight * 2.2}")
elif weight_unit.upper() == "L":
    print(f"Your weight in Kgs is {weight / 2.2}")
else:
    print("Specify your weight unit correctly!")

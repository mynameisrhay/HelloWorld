# 8th exercise, a bit intermediate. use for loop to type the letter F with *. there's a premeditated list
# [5, 2, 5, 2, 2]. multiplying * with the numbers on list to print it is forbidden. only using for loop is allowed.

numbers = [5, 2, 5, 2, 2]

for i in numbers:
    char = ""
    for x in range(i):
        char += "x"
    print(char)

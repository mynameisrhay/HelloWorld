# 9th exercise. must make a program to find the largest number on a list. must not use the max command.

numbers = [1, 5, 6, 8, 8, 6, 4, 9, 12, 7]

i = 0
max_num = numbers[0]
while not i == len(numbers):
    if numbers[i] > max_num:
        max_num = numbers[i]
    i += 1

print("Largest number is " + str(max_num))

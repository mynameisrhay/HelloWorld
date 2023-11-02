# 10th exercise. remove duplicates on a list. will use for loop for this exercise.

numbers = [1, 2, 4, 6, 6, 7, 7, 3, 7, 2, 8, 9, 10]
unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)
unique.sort()
print(unique)

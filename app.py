numbers = [2, 2, 4, 3, 4, 1, 7, 9]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
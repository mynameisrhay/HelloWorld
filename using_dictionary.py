# 11th exercise. using dictionary, make a program where the phone number will be translated from numbers to words

phone = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}

number = input("Phone: ")
value = ""
for char in number:
    value += phone.get(char, "*") + " "
print(value)

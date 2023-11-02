# 12th exercise. need to use the code number to words converter and make it a reusable function

def num_converter(number):
    value = ""
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
    for char in number:
        value += phone.get(char, "*") + " "
    return value


ch = input("Phone: ")
print(num_converter(ch))

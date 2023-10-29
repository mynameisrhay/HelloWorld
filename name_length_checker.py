# 4th exercise. name validator. if name is less than 3 characters, prompt the user that it must be at least 3 characters. If more than 50 characters, prompt user that it must be a maximum of 50 characters.

username = input("Name: ")

if len(username) < 3:
    print("Username must be at least 3 characters")
elif len(username) > 50:
    print("Username must be a maximum of 50 characters")
else:
    print("Username looks good!")

def greet_user(first_name, last_name):
    print(f"Hello {first_name} {last_name}!")
    return first_name + " " + last_name


full_name = ""
full_name = greet_user("John", "Smith")
print(f"Full name based on greet_user function is {full_name}")

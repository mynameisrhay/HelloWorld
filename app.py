# practice path and libraries. will use pathlib module

from pathlib import Path

dir_name = input("Input the name of the directory that you want to create: ")
path = Path(dir_name)

response = input(f"Create '{dir_name}' folder? (Y/N): ")
if response.upper() == "Y":
    if not path.exists():
        path.mkdir()
        print(f"Created the '{dir_name}' folder.")
    else:
        print(f"{dir_name} folder already exists")
    response = input(f"Delete '{dir_name}' folder? (Y/N): ")
    if response.upper() == "Y":
        if path.exists():
            path.rmdir()
            print(f"Removed the '{dir_name}' folder.")
        else:
            print(f"'{dir_name}' folder does not exists")
    else:
        print(f"Did not delete the {dir_name} folder.")

print("Printing out the files in the current directory: ")
path = Path()
for file in path.glob("*"):
    print(file)

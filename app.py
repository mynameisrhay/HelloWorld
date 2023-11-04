# practice path and libraries. will use pathlib module

from pathlib import Path

path = Path("emails")

response = input("Create 'emails' folder? (Y/N): ")
if response.upper() == "Y":
    if not path.exists():
        path.mkdir()
        print("Created the 'emails' folder.")
        response = input("Delete 'emails' folder? (Y/N): ")
        if response.upper() == "Y":
            if not path.exists():
                path.rmdir()
                print("Removed the 'emails' folder.")
            else:
                print("'emails' folder does not exists")
    else:
        print("emails folder already exists")

# 6th exercise. simple car game that has 4 functions, start, stop, help, and quit. must exercise while loop
# and if functions effectively.

while True:
    command = input("> ").lower()
    if command == "help":
        print("""start - to start the car
stop - to stop the car
quit - to end the application""")
    elif command == "start":
        print("Car has started")
    elif command == "stop":
        print("Car has stopped")
    elif command == "quit":
        print("Thanks for playing!")
        break
    else:
        print("Sorry, I don't understand that")

# 6th exercise. simple car game that has 4 functions, start, stop, help, and quit. must exercise while loop
# and if functions effectively.

car_started = False

while True:
    command = input("> ").lower()
    if command == "help":
        print("""start - to start the car
stop - to stop the car
quit - to end the application""")
    elif command == "start":
        if not car_started:
            print("Car has started")
            car_started = True
        else:
            print("Car has already started.")
    elif command == "stop":
        if car_started:
            print("Car has stopped")
            car_started = False
        else:
            print("Car has already stopped.")
    elif command == "quit":
        print("Thanks for playing!")
        break
    else:
        print("Sorry, I don't understand that. Type 'help' for the available commands.")

########################Car Game######################

command = ""
started = False
while True:
    prevCommand = command
    command = input(">").lower() 
    if command == 'start':
        if started:
            print("Car has already started")
        else:
            started = True
            print("Car started...Ready to go!")
    elif command == 'stop':
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped.")  
    elif command == 'help':
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == 'quit':
        break
    else:
        print("I don't understand that...")
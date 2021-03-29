#!/usr/bin/env python3

print ("Name: Sean Naatz")

password_database = {"Username" : "dnedry","Password" : "please"}

command_database = {"reboot" : "OK. I will reboot all park systems."}
command_database["shutdown"] = "OK. I will shut down all park systems."
command_database["done"] = "I hate all this hacker stuff."

white_rabbit_object = 0
counter = 0

while white_rabbit_object == 0 and counter <= 2:
    input_user = input("Username: ")
    input_password = input("Password: ")

    if input_user == password_database["Username"] and input_password == password_database["Password"]:
        white_rabbit_object = white_rabbit_object + 1
        print("Hi, Dennis. You're still the best hacker in Jurassic Park.")

        input_command = input(f"Please enter a command: {command_database.keys()}: ")

        if input_command == "reboot":
            print(command_database["reboot"])

        elif input_command == "shutdown":
            print(command_database["shutdown"])

        elif input_command == "done":
            print(command_database["done"])

        else:
            print("The Lysine Contingency has been put into effect.")

    elif input_user != password_database["Username"] or input_password != password_database["Password"]:
        counter = counter + 1
        if counter == 3:
            break
        else:
            print(f"You didn't say the magic word. {counter}")

if counter == 3:
    print("You didn't say the magic word!\n"*25)

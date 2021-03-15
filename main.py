from pynput.keyboard import Key, Controller
from pynput import keyboard

print("autoclicker v1.0.0")
print("by aejester (https://github.com/aejester)\n\n")

def choice():
    print("""Choose an option:
    1: Run a profile
    2: Create a profile
    3: Remove a profile
    4: Edit setting
    """)

    choice = input("> ")

    return int(choice)

while True:
    initial = choice()

    if initial == 1:
        profiles = open(".profiles", "r").read().split("\n")

        i = 0
        print("Select a profile: ")
        for profile in profiles:
            print("\t"+str(i+1)+": "+profile)

        profile = int(input("> ")) - 1 



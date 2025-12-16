import random
from colorama import init
import platform
import psutil
import time
from datetime import datetime
import os
import sys

versionOS = 1.6
nts1 = str()
nts2 = str()
nts3 = str()
nts4 = str()
nts5 = str()

endless = 0
start_time = time.time()


def loading():
    print(Fore.GREEN)
    print("Loading...")
    print(Fore.WHITE)


def clear():
    os.system("cls" if os.name == "nt" else "clear")


from colorama import Fore, Back, Style

while endless == 0:
    loading()
    time.sleep(2)
    clear()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Welcome to" + Fore.BLUE + " Gullie OS!")
    print(Fore.BLUE)
    print("Current time:", current_time)
    print(Fore.WHITE)
    print("Choose an action:")
    print("1.Launch Calculator")
    print("2.Launch Game Launcher")
    print("3.Info")
    print("4.Launch Notes")
    print("5.Power Off")
    programm = input()
    loading()
    time.sleep(2)
    clear()

    # Calculator
    if programm == "1":
        print("Welcome to " + Fore.BLUE + "Gullie Calculator!")
        print(Fore.WHITE)
        print("Choose an action:")
        print("+,-,/,*")
        action = input()
        if action == "+":
            a = float(input("First number: "))
            b = float(input("Second number: "))
            c = a + b
            loading()
            time.sleep(2)
            print("Result: " + str(c))
        elif action == "-":
            a = float(input("First number: "))
            b = float(input("Second number: "))
            c = a - b
            loading()
            time.sleep(2)
            print("Result: " + str(c))
        elif action == "/":
            a = float(input("First number: "))
            b = float(input("Second number: "))
            if b == 0:
                print(Fore.RED)
                print("ERROR!")
            else:
                c = a / b
                loading()
                time.sleep(2)
                print("Result: " + str(c))
        elif action == "*":
            a = float(input("First number: "))
            b = float(input("Second number: "))
            c = a * b
            loading()
            time.sleep(2)
            print("Result: " + str(c))
        else:
            print(Fore.RED)
            print("ERROR!")
        input()

    # Game Launcher
    elif programm == "2":
        print("Welcome to " + Fore.BLUE + "Gullie Game Launcher!")
        print(Fore.WHITE)
        print("Choose a game:")
        print("1.Guess the number")
        print("2.Come up with a number")
        game = input()
        if game == "1":
            loading()
            time.sleep(2)
            clear()
            print("Welcome to " + Fore.BLUE + "Guess the number!")
            print(Fore.WHITE)
            print("Your task is to guess the number up to 10 that I came up with.")
            print(Fore.RED)
            print("Start?")
            print(Fore.WHITE + "1.Yes")
            print("2.No")
            yon = input()
            if yon == "1":
                print("Now the number will be invented")
                loading()
                time.sleep(2)
                print("The number was invented")
                num = random.randint(1, 10)
                plrnum = float(input("Your answer: "))
                if plrnum == num:
                    print("You guessed the number(" + str(num) + ")")
                else:
                    print("You did not guess the number " + str(num))
            elif yon >= str(3):
                print(Fore.RED)
                print("ERROR!")
        elif game == "2":
            loading()
            time.sleep(2)
            clear()
            print("Welcome to " + Fore.BLUE + "Come up with a number!")
            print(Fore.WHITE)
            print(
                "Your task is to come up with a number up to 10, and mine is to guess this number."
            )
            print(Fore.RED)
            print("Start?")
            print(Fore.WHITE + "1.Yes")
            print("2.No")
            yon2 = input()
            if yon2 == "1":
                plrnumc = input("Your number:")
                loading()
                time.sleep(2)
                numc = random.randint(1, 10)
                if plrnumc == numc:
                    print("Hooray, I guessed the number " + str(numc))
                else:
                    print(
                        "It's a pity I didn't guess the number, I thought it was: "
                        + str(numc)
                    )
            elif yon2 >= str(3):
                print(Fore.RED)
                print("ERROR!")
        elif game >= "3":
            print(Fore.RED)
            print("ERROR!")
        input()

    # info
    elif programm == "3":
        hostname = (platform.node(),)
        numofcor = (psutil.cpu_count(logical=False),)
        architecture = platform.architecture()
        processor = (platform.processor(),)
        RAM = (round(psutil.virtual_memory().total / (1024**3), 2),)
        seanstimenr = time.time() - start_time
        seanstime_rounded = round(seanstimenr)
        print(
            f"//////////////////{Fore.BLUE} G U L L I E    I N F O {Fore.WHITE}//////////////////"
        )
        print("OS: Gullie")
        print("OS Version: " + str(versionOS))
        print("Host name: " + str(hostname))
        print("Architecture: " + str(architecture))
        print("Processor: " + str(processor))
        print("Number of cores: " + str(numofcor))
        print("RAM: " + str(RAM))
        print(f"Session duration: {seanstime_rounded} seconds")
        input()

    # Notes
    elif programm == "4":
        print("Welcome to " + Fore.BLUE + "Gullie Notes!")
        print(Fore.WHITE)
        print("Choose an action:")
        print("1.View notes")
        print("2.Write a note")
        print("3.Сlear notes")
        actnot = input()
        if actnot == "1":
            loading()
            time.sleep(2)
            clear()
            print("Notes:")
            print("1." + nts1)
            print("2." + nts2)
            print("3." + nts3)
            print("4." + nts4)
            print("5." + nts5)
        elif actnot == "2":
            loading()
            time.sleep(2)
            clear()
            print("Enter a note:")
            note = input()
            loading()
            time.sleep(2)
            print("Select the slot to save the note:")
            print("1,2,3,4,5")
            sslot = input()
            if sslot == "1":
                nts1 = note
                print("Note saved")
            elif sslot == "2":
                nts2 = note
                print("Note saved")
            elif sslot == "3":
                nts3 = note
                print("Note saved")
            elif sslot == "4":
                nts4 = note
                print("Note saved")
            elif sslot == "5":
                nts5 = note
                print("Note saved")
        elif actnot == "3":
            nts1 = str()
            nts2 = str()
            nts3 = str()
            nts4 = str()
            nts5 = str()
            print("The notes are cleaned")
        input()

    # PowerOff
    elif programm == "5":
        loading()
        time.sleep(2)
        sys.exit()

    else:
        print(Fore.RED)
        print("ERROR!")
        time.sleep(1)
        clear()


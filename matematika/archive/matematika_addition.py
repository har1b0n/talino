import datetime
import time
import random
from matematika_functions import clear_console

def choose_level():
    fancy_level = """
    \033[1;31m===============================================
    \033[1;36m              LEVEL
    \033[1;31m===============================================
    \033[1;32m 1 - Beginner (0-5)
    \033[1;32m 2 - Easy (0-10)
    \033[1;32m 3 - Normal (0-100)
    \033[1;32m 4 - Hard (0-1000)
    \033[1;31m===============================================
    """
    print(fancy_level)
    while True:
        try:
            return int(input("\033[1;37mEnter your choice: "))
        except ValueError:
            print("\033[1;31mInvalid entry. Please enter a valid number.")

def perform_addition(level, sanitized_name):
    clear_console()

    results_file = f"addition_results_{sanitized_name}.txt"
    highscore_file = f"addition_highscore_{sanitized_name}.txt"    

    # Open a file to write the output
    with open(results_file, "a") as f1,open(highscore_file, "a") as f2:
        print("\n\033[1;31mYou chose addition. Lets Go!")

        #Configuration
        startTime = datetime.datetime.now()
        hs = 0
        x = 10
        y = 0
        n = 0
        
        match level:
            case 1:
                l = 0
                h = 5
            case 2:
                l = 0
                h = 10
            case 3:
                l = 0
                h = 100
            case 4:
                l = 0
                h = 1000
            case _:  # Handles any invalid input
                print("\033[1;31mInvalid choice. Please choose a valid option.")

        for counter in range(x):
            a = random.randint(l, h)
            b = random.randint(l, h)
            print(f"\033[1;34m Score: {y}/{counter}")
            print("\n\033[1;37m===============================================")
            print(f"  {a} + {b} ")
            correctAnswer = a + b
            print("\033[1;37m===============================================")

            # Start tracking the time
            questionStart = datetime.datetime.now()
            answer = None
            while answer is None:
                try:
                    answer = int(input("\033[1;37m Enter your answer: "))
                except ValueError:
                    print("\033[1;31m Invalid Entry \033[1;30m")
                # End tracking the time and calculate the duration
            questionEnd = datetime.datetime.now()
            timeTaken = questionEnd - questionStart  # Calculate how long they took

            if correctAnswer == answer:
                print(f"\033[1;32m You are correct. The answer is {correctAnswer}")
                y += 1
                f1.write(f"{sanitized_name},Question {counter+1},{a} + {b} = {answer},Correct,{timeTaken}\n")
            else:
                print(f"\033[1;31m You are wrong. The answer is {correctAnswer}")
                n += 1
                f1.write(f"{sanitized_name},Question {counter+1},{a} + {b} = {answer},Wrong,{timeTaken}\n")
            time.sleep(1)
            clear_console()

        endTime = datetime.datetime.now()
        final_score = f"\033[1;34mFinal Score: {y}/{x}"

        clear_console()
        print("\033[1;37m===============================================")
        print("ADDITION     ")
        print(final_score)
        print("\033[1;37m===============================================")
        f2.write(f"{sanitized_name},{y}/{x},{startTime}\n")

def perform_subtraction(level, sanitized_name):
    clear_console()

    results_file = f"subtraction_results_{sanitized_name}.txt"
    highscore_file = f"subtraction_highscore_{sanitized_name}.txt"    

    # Open a file to write the output
    with open(results_file, "a") as f1,open(highscore_file, "a") as f2:
        print("\n\033[1;31mYou chose subtraction. Lets Go!")

        #Configuration
        startTime = datetime.datetime.now()
        hs = 0
        x = 10
        y = 0
        n = 0
        
        match level:
            case 1:
                l = 0
                h = 5
            case 2:
                l = 0
                h = 10
            case 3:
                l = 0
                h = 15
            case 4:
                l = 0
                h = 20
            case _:  # Handles any invalid input
                print("\033[1;31mInvalid choice. Please choose a valid option.")

        for counter in range(x):
            a = random.randint(l, h)
            b = random.randint(l, h)

            # Ensure non-negative result by swapping a and b if necessary
            if b > a:
                a, b = b, a

            print(f"\033[1;34m Score: {y}/{counter}")
            print("\n\033[1;37m===============================================")
            print(f"  {a} - {b} ")
            correctAnswer = a - b
            print("\033[1;37m===============================================")

            # Start tracking the time
            questionStart = datetime.datetime.now()
            answer = None
            while answer is None:
                try:
                    answer = int(input("\033[1;37mEnter your answer: "))
                except ValueError:
                    print("\033[1;31mInvalid Entry \033[1;30m")
                # End tracking the time and calculate the duration
            questionEnd = datetime.datetime.now()
            timeTaken = questionEnd - questionStart  # Calculate how long they took

            if correctAnswer == answer:
                print(f"\033[1;32m You are correct. The answer is {correctAnswer}")
                y += 1
                f1.write(f"{sanitized_name},Question {counter+1},{a} - {b} = {answer},Correct,{timeTaken}\n")
            else:
                print(f"\033[1;31m You are wrong. The answer is {correctAnswer}")
                n += 1
                f1.write(f"{sanitized_name},Question {counter+1},{a} - {b} = {answer},Wrong,{timeTaken}\n")
            time.sleep(1)
            clear_console()

        endTime = datetime.datetime.now()
        final_score = f"\033[1;34mFinal Score: {y}/{x}"

        clear_console()
        print("\033[1;37m===============================================")
        print("SUBTRACTION")
        print(final_score)
        print("\033[1;37m===============================================")
        f2.write(f"{sanitized_name},{y}/{x},{startTime}\n")
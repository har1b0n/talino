import os
import random
import datetime
import re

os.system('cls' if os.name == 'nt' else 'clear')
yourname = input("\033[1;37mEnter your name: ").strip()
sanitized_name = re.sub(r'[^\w\-_.]', '_', yourname)

exit = 'n'
while exit == 'n':

    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"\n\033[1;37m Welcome \033[1;31m{sanitized_name}\033[1;37m,choose from the following option.")
    print("1 - Addition")
    print("2 - Substraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Counting")
    try:
        choice1 = int(input("Enter your choice: "))
    except ValueError:
        print("\033[1;31mInvalid entry. Please enter a valid number.")
        continue  # Re-loop to show the menu again

    match choice1:
        case 1:
            os.system('cls' if os.name == 'nt' else 'clear')

            print("1 - Beginner (0-5)")
            print("2 - Easy (0-10)")
            print("3 - Normal (0-100)")
            print("4 - Hard (0-1000)")
            try:
                level = int(input("Enter your choice: "))
            except ValueError:
                print("\033[1;31mInvalid entry. Please enter a valid number.")
                continue  # Re-loop to show the menu again
            
            results_file = f"addition_results_{sanitized_name}.txt"
            highscore_file = f"addition_highscore_{sanitized_name}.txt"    

            # Open a file to write the output
            with open(results_file, "a") as f1,open(highscore_file, "a") as f2:
                print("\n\033[1;31mYou chose addition. Lets Go!")

                #Configuration
                startTime = datetime.datetime.now()
                hs = 0
                x = 20
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
                    print("\n\033[1;37m**********************************")
                    print(f"  {a} + {b} ")
                    correctAnswer = a + b
                    print("\033[1;37m**********************************\033[1;30m")

                    # Start tracking the time
                    questionStart = datetime.datetime.now()
                    answer = None
                    while answer is None:
                        try:
                            answer = int(input("Enter your answer: "))
                        except ValueError:
                            print("\033[1;31m Invalid Entry \033[1;30m")
                     # End tracking the time and calculate the duration
                    questionEnd = datetime.datetime.now()
                    timeTaken = questionEnd - questionStart  # Calculate how long they took

                    if correctAnswer == answer:
                        print(f"\033[1;32m You are correct. The answer is {correctAnswer}")
                        y += 1
                        f1.write(f"{yourname},Question {counter+1},{a} + {b} = {answer},Correct,{timeTaken}\n")
                    else:
                        print(f"\033[1;31m You are wrong. The answer is {correctAnswer}")
                        n += 1
                        f1.write(f"{yourname},Question {counter+1},{a} + {b} = {answer},Wrong,{timeTaken}\n")
                    print(f"\033[1;34m Score: {y}/{counter+1}\n")

                endTime = datetime.datetime.now()
                final_score = f"\n \033[1;34m Final Score: {y}/{x}\n"
                print("\033[1;37m ***********************")
                print(final_score)
                print("\033[1;37m ***********************")
                f2.write(f"{yourname},{y}/{x},{startTime}\n")

        case 2:
            os.system('cls' if os.name == 'nt' else 'clear')

            print("1 - Beginner (0-5)")
            print("2 - Easy (0-10)")
            print("3 - Normal (0-100)")
            print("4 - Hard (0-1000)")
            try:
                level = int(input("Enter your choice: "))
            except ValueError:
                print("\033[1;31mInvalid entry. Please enter a valid number.")
                continue  # Re-loop to show the menu again

            results_file = f"subtraction_results_{sanitized_name}.txt"
            highscore_file = f"subtraction_highscore_{sanitized_name}.txt" 

            # Open a file to write the output
            with open(results_file, "a") as f1,open(highscore_file, "a") as f2:
                print("\n\033[1;31mYou chose subtraction. Lets Go!")

                #Configuration
                startTime = datetime.datetime.now()
                hs = 0
                x = 20
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

                    print("\n\033[1;37m**********************************")
                    print(f"  {a} - {b} ")
                    correctAnswer = a - b
                    print("\033[1;37m**********************************\033[1;30m")

                    # Start tracking the time
                    questionStart = datetime.datetime.now()
                    answer = None
                    while answer is None:
                        try:
                            answer = int(input("Enter your answer: "))
                        except ValueError:
                            print("\033[1;31m Invalid Entry \033[1;30m")
                    # End tracking the time and calculate the duration
                    questionEnd = datetime.datetime.now()
                    timeTaken = questionEnd - questionStart  # Calculate how long they took

                    if correctAnswer == answer:
                        print(f"\033[1;32m You are correct. The answer is {correctAnswer}")
                        y += 1
                        f1.write(f"{yourname},Question {counter+1},{a} - {b} = {answer},Correct,{timeTaken}\n")
                    else:
                        print(f"\033[1;31m You are wrong. The answer is {correctAnswer}")
                        n += 1
                        f1.write(f"{yourname},Question {counter+1},{a} - {b} = {answer},Wrong,{timeTaken}\n")
                    print(f"\033[1;34m Score: {y}/{counter+1}\n")

                endTime = datetime.datetime.now()
                final_score = f"\n \033[1;34m Final Score: {y}/{x}\n"
                print("\033[1;37m ***********************")
                print(final_score)
                print("\033[1;37m ***********************")
                f2.write(f"{yourname},{y}/{x},{startTime}\n")

        case 3:
            os.system('cls' if os.name == 'nt' else 'clear')

            print("1 - Beginner (0-5)")
            print("2 - Easy (0-10)")
            print("3 - Normal (0-50)")
            print("4 - Hard (0-100)")
            try:
                level = int(input("Enter your choice: "))
            except ValueError:
                print("\033[1;31mInvalid entry. Please enter a valid number.")
                continue  # Re-loop to show the menu again

            results_file = f"multiplication_results_{sanitized_name}.txt"
            highscore_file = f"multiplication_highscore_{sanitized_name}.txt" 

            # Open a file to write the output
            with open(results_file, "a") as f1,open(highscore_file, "a") as f2:
                print("\n\033[1;31mYou chose multiplication. Lets Go!")

                #Configuration
                startTime = datetime.datetime.now()
                hs = 0
                x = 20
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
                        h = 50
                    case 4:
                        l = 0
                        h = 100
                    case _:  # Handles any invalid input
                        print("\033[1;31mInvalid choice. Please choose a valid option.")

                for counter in range(x):
                    a = random.randint(l, h)
                    b = random.randint(l, h)
                    print("\n\033[1;37m**********************************")
                    print(f"  {a} * {b} ")
                    correctAnswer = a * b
                    print("\033[1;37m**********************************\033[1;30m")

                    # Start tracking the time
                    questionStart = datetime.datetime.now()
                    answer = None
                    while answer is None:
                        try:
                            answer = int(input("Enter your answer: "))
                        except ValueError:
                            print("\033[1;31m Invalid Entry \033[1;30m")
                     # End tracking the time and calculate the duration
                    questionEnd = datetime.datetime.now()
                    timeTaken = questionEnd - questionStart  # Calculate how long they took

                    if correctAnswer == answer:
                        print(f"\033[1;32m You are correct. The answer is {correctAnswer}")
                        y += 1
                        f1.write(f"{yourname},Question {counter+1},{a} * {b} = {answer},Correct,{timeTaken}\n")
                    else:
                        print(f"\033[1;31m You are wrong. The answer is {correctAnswer}")
                        n += 1
                        f1.write(f"{yourname},Question {counter+1},{a} * {b} = {answer},Wrong,{timeTaken}\n")
                    print(f"\033[1;34m Score: {y}/{counter+1}\n")

                endTime = datetime.datetime.now()
                final_score = f"\n \033[1;34m Final Score: {y}/{x}\n"
                print("\033[1;37m ***********************")
                print(final_score)
                print("\033[1;37m ***********************")
                f2.write(f"{yourname},{y}/{x},{startTime}\n")

        case 4:
            os.system('cls' if os.name == 'nt' else 'clear')

            print("1 - Beginner (0-5)")
            print("2 - Easy (0-10)")
            print("3 - Normal (0-50)")
            print("4 - Hard (0-100)")
            try:
                level = int(input("Enter your choice: "))
            except ValueError:
                print("\033[1;31mInvalid entry. Please enter a valid number.")
                continue  # Re-loop to show the menu again

            results_file = f"division_results_{sanitized_name}.txt"
            highscore_file = f"division_highscore_{sanitized_name}.txt" 

            # Open a file to write the output
            with open(results_file, "a") as f1,open(highscore_file, "a") as f2:
                print("\n\033[1;31mYou chose division. Lets Go!")

                #Configuration
                startTime = datetime.datetime.now()
                hs = 0
                x = 20
                y = 0
                n = 0
                
                match level:
                    case 1:
                        l = 1
                        h = 5
                    case 2:
                        l = 1
                        h = 10
                    case 3:
                        l = 1
                        h = 50
                    case 4:
                        l = 1
                        h = 100
                    case _:  # Handles any invalid input
                        print("\033[1;31mInvalid choice. Please choose a valid option.")

                for counter in range(x):

                    b = random.randint(l, h)  # Generate divisor
                    multiplier = random.randint(l, h)  # Generate a random multiplier
                    a = b * multiplier  # Ensure a is divisible by b
    
                    print("\n\033[1;37m**********************************")
                    print(f"  {a} / {b} ")
                    correctAnswer = a / b
                    print("\033[1;37m**********************************\033[1;30m")

                    # Start tracking the time
                    questionStart = datetime.datetime.now()
                    answer = None
                    while answer is None:
                        try:
                            answer = int(input("Enter your answer: "))
                        except ValueError:
                            print("\033[1;31m Invalid Entry \033[1;30m")
                     # End tracking the time and calculate the duration
                    questionEnd = datetime.datetime.now()
                    timeTaken = questionEnd - questionStart  # Calculate how long they took

                    if correctAnswer == answer:
                        print(f"\033[1;32m You are correct. The answer is {correctAnswer}")
                        y += 1
                        f1.write(f"{yourname},Question {counter+1},{a} / {b} = {answer},Correct,{timeTaken}\n")
                    else:
                        print(f"\033[1;31m You are wrong. The answer is {correctAnswer}")
                        n += 1
                        f1.write(f"{yourname},Question {counter+1},{a} / {b} = {answer},Wrong,{timeTaken}\n")
                    print(f"\033[1;34m Score: {y}/{counter+1}\n")

                endTime = datetime.datetime.now()
                final_score = f"\n \033[1;34m Final Score: {y}/{x}\n"
                print("\033[1;37m ***********************")
                print(final_score)
                print("\033[1;37m ***********************")
                f2.write(f"{yourname},{y}/{x},{startTime}\n")

        
        case 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n\033[1;31mYou chose counting. Lets Go!\n")

            #Configuration
            y = 0
            n = 0

            for counter in range(10):
                print("\n")
                x = random.randint(1, 20)
                for barcounter in range(x):
                    #\u2588,\u265E,\u1F535
                    blocks = print("\033[1;34m \u265E ", end=" ")
                    if barcounter == 9:
                        print("\n")
                
                correctAnswer = x

                answer = None
                while answer is None:
                    try:
                        answer = int(input("\n\n\033[1;37mEnter your answer: "))
                    except ValueError:
                        print("\033[1;31m Invalid Entry \033[1;30m")
                
                if correctAnswer == answer:
                    y += 1
                    print(f"\033[1;32m You are correct. The answer is {correctAnswer}")
                else:
                    n += 1
                    print(f"\033[1;31m You are wrong. The answer is {correctAnswer}")
                
                print(f"\033[1;34m Score: {y}/{counter+1}\n")

        case _:  # Handles any invalid input
            print("\033[1;31mInvalid choice. Please choose a valid option.")

    print("\033[1;34m")
    exit = input("\n\033[1;37mDo you want to exit the game? (y/n): ")
    if exit.lower() == 'y':
        print("\033[1;37mThank you for playing.\n")
        break

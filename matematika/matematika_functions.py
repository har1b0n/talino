import os
import time

def clear_console():
    #clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome_screen():
    clear_console() 
    launch_patterns = [
      "/ M",
      "- MA",
      "\ MAT",
      "| MATE",  
      "/ MATEM",
      "- MATEMA",
      "\ MATEMAT",
      "| MATEMATI",
      "/ MATEMATIK",
      "- MATEMATIKA"
    ] 

    fancy_text = """
    \033[1;31m===============================================
    \033[1;36m  WELCOME TO THE MATEMATIKA CHALLENGE!  
    \033[1;31m===============================================
    \033[1;32m        Sharpen your math skills and rise     
    \033[1;32m         to the top of the leaderboard!       
    \033[1;31m===============================================
    """
    
    for pattern in launch_patterns:
        print(f"\033[1;37m{pattern}")  
        time.sleep(0.3)  
        clear_console()
    
    print(fancy_text)
    time.sleep(1)  

def main_menu():
    fancy_mainmenu = """
    \033[1;31m===============================================
    \033[1;36m              MAIN MENU
    \033[1;31m===============================================
    \033[1;32m 1 - Addition
    \033[1;32m 2 - Substraction
    \033[1;32m 3 - Multiplication
    \033[1;32m 4 - Division
    \033[1;32m 5 - Counting       
    \033[1;31m===============================================
    """
    print(fancy_mainmenu)
    while True:
        try:
            print("\033[1;37m Choose from the following option.")
            choice = int(input("\033[1;37m Enter your choice: "))
            return choice
        except ValueError:
            print("\033[1;31m Invalid entry. Please enter a valid number.")
    time.sleep(1) 


def goodbye_screen():
    clear_console() 
    fancy_goodbye = """
    \033[1;33m===============================================
    \033[1;34m         THANK YOU FOR PLAYING THE GAME!       
    \033[1;33m===============================================
    \033[1;35m            Hope to see you again soon!        
    \033[1;33m===============================================
    """
    print(fancy_goodbye)
    time.sleep(1) 
  
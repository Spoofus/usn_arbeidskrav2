#!/usr/bin/env python
# Second mandatory coding assignment in the USN course for Python introduction
# Author Anders Bakken / bakken.anders@gmail.com
# Assignment consists of several subtasks. Therefore this program is built up using Objects (class) where Main is a controller
# the subtasks are separated into respective classes with the logic and methods

#Impprt the subtasks classes
from Oppg_1 import Oppg_1
from Oppg_2 import Oppg_2
from Oppg_3 import Oppg_3
from Oppg_4 import Oppg_4
from Oppg_5 import Oppg_5
from Oppg_6 import Oppg_6

class Main():
    """Controller class for managing and running subtasks."""
    def __init__(self):
        self.oppg_1 = Oppg_1()
        self.oppg_2 = Oppg_2()
        self.oppg_3 = Oppg_3()
        self.oppg_4 = Oppg_4()
        self.oppg_5 = Oppg_5()
        self.oppg_6 = Oppg_6()
        
    def display_menu(self):
        """Displays the main menu options."""
        print("\nMain Menu:")
        print("1. Assignment 1 - Calculate age")
        print("2. Assignment 2 - Calculate number of pizza needed")
        print("3. Assignment 3 - Convert Grade to Radient")
        print("4. Assignment 4 - Add or lookup Country in dataset")
        print("5. Assignment 5 - Calculate the area of a circle")
        print("6. Assignment 6 - Calculate something something")
        print("7. Exit")
    
    def execute_choice(self, choice):
        if choice == 1:
            self.oppg_1.run()
        elif choice == 2:
            self.oppg_2.run()
        elif choice == 3:
            self.oppg_3.run()
        elif choice == 4:
            self.oppg_4.run()
        elif choice == 5:
            self.oppg_5.run()
        elif choice == 6:
            self.oppg_6.run()
        elif choice == 7:
            print("Exiting the program. Goodbye!")
        else:
            print("Invalid choice. Please try again.")

    def run(self):
        """Run the main program. Display menu and execute command."""
        print("Running Program :")
        #self.oppg_1.run()
        while True:
            self.display_menu()
            try:
                choice = int(input("Enter your choice (1-7): "))
                if choice == 7:
                    break
                self.execute_choice(choice)
            except ValueError:
                print("Please enter a valid number.")

def main():
    controller = Main()
    controller.run()

if __name__ == "__main__":
    main()
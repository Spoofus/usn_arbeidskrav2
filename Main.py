#!/usr/bin/env python
# Second mandatory coding assignment in the USN course for Python introduction
# Author Anders Bakken / bakken.anders@gmail.com
# Assignment consists of several subtasks. Therefore this program is built up using Objects (class) where Main is a controller
# the subtasks are separated into respective classes with the logic and methods

from Oppg_1 import Oppg_1
from Oppg_2 import Oppg_2

class Main():
    """Controller class for managing and running subtasks."""
    def __init__(self):
        self.oppg_1 = Oppg_1()
        self.oppg_2 = Oppg_2()
        
    def display_menu(self):
        """Displays the main menu options."""
        print("\nMain Menu:")
        print("1. Assignment 1 - Calculate age")
        print("2. Assignment 2 - Calculate number of pizza needed")
        print("3. Object2 - Method1")
        print("4. Object2 - Method2")
        print("5. Exit")
    
    def execute_choice(self, choice):
        if choice == 1:
            self.oppg_1.run()
        elif choice == 2:
            self.oppg_2.run()
        elif choice == 3:
            self.object2.method1()
        elif choice == 4:
            self.object2.method2()
        elif choice == 5:
            print("Exiting the program. Goodbye!")
        else:
            print("Invalid choice. Please try again.")

    def run(self):
        """Run the main program. Display menu and execute command."""
        print("Running Oppgave 1:")
        #self.oppg_1.run()
        while True:
            self.display_menu()
            try:
                choice = int(input("Enter your choice (1-5): "))
                if choice == 5:
                    break
                self.execute_choice(choice)
            except ValueError:
                print("Please enter a valid number.")

def main():
    controller = Main()
    controller.run()

if __name__ == "__main__":
    main()
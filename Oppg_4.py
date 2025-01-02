#!/usr/bin/env
# Second mandatory coding assignment in the USN course for Python introduction
# Author Anders Bakken / bakken.anders@gmail.com
# Taking age as input and calculate how many pizzaz you would need to purchase based on people eating 1/4 each

import math

class Oppg_4():
    def __init__(self):
        self.data = {
            "Norway": ["Oslo", 0.634 ],
            "England": ["London", 8.982],
            "France": ["Paris", 2.161],
            "Italy": ["Rome", 2.873]
        }

    def run(self):
        try:
            while True:
                self.callUser()
                user_input = input("Enter value: ")
                user_input = int(user_input)
                if not (1 <= user_input <= 2):
                    print("Invalid input. Exiting")
                    break
                else:
                    if user_input == 1:
                        self.runLookup()
                    elif user_input == 2:
                        self.runExtendData()
        except Exception as e:
            print(f"An error occured: {e}")
    
    #Ask for user for lookup in the dataset or add to the dataset
    def callUser(self):
        """
        Prompts the user with options to either look up a country in the dataset or add a country to the dataset.

        Options:
        1. Lookup a country in the dataset.
        2. Add a country to the dataset.
        """
        
        print("\nDo you want to lookup a country in the dataset: Press 1")
        print("Do you want to add a country to the dataset: Press 2")
        print("Any other values will exit the program")
                  
    def runLookup(self):
        try:
            user_input = input("Enter name of country you would lookup: ")
            if user_input in self.data:
                print(f'Capital of {user_input} are {self.data[user_input][0]} and the pupulation is {self.data[user_input][1]} in millions')
        except ValueError:
            print("Invalid input.")
        except Exception as e:
            print(f"An error occured: {e}")

    def runExtendData(self):
        try:
            user_input = input("Enter name of country you would add: ")
            if user_input in self.data:
                print("Country "+user_input +" already exists in dataset")
            else:
                capital = input(f'Enter the capital of {user_input}: ')
                population = input("Enter the population in millions: ")
                self.data[user_input] = [capital, population]
                print(f'Country added to dataset' )
        except Exception as e:
            print(f"An error occured: {e}")
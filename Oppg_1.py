#!/usr/bin/env#-
# Second mandatory coding assignment in the USN course for Python introduction#-
# Author Anders Bakken / bakken.anders@gmail.com#-
# Taking age as input and calculate how old you are#-
# Note: The assignment says that you should calculate from year 2024. This program will calucate out of the year SYSDATE

from datetime import datetime


class Oppg_1():
    def __init__(self):
        self.current_year = datetime.now().year

    def calculate_age(self, birth_year):
        age = self.current_year - birth_year
        return age

    def run(self):
        try:
            birth_year = int(input("Enter your birth year: "))
            age = self.calculate_age(birth_year)
            print(f"You are {age} years old.")
        except ValueError:
            print("Invalid input. Please enter a valid birth year (e.g., 1981).")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
#!/usr/bin/env
# Second mandatory coding assignment in the USN course for Python introduction
# Author Anders Bakken / bakken.anders@gmail.com
# Taking age as input and calculate how many pizzaz you would need to purchase based on people eating 1/4 each

import math

class Oppg_2():
    def __init__(self):
        pizza_demand = 0
    
    def run(self):
        try:
            number_of_students = int(input("Number of students "))
            pizza_demand = math.ceil(number_of_students / 4)
            print(f'Det må handles inn {pizza_demand} pizzaer til festen.')
        except ValueError:
            print("Invalid input. Please enter a valid number of students in Integer")

            
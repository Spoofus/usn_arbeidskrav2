#!/usr/bin/env
# Second mandatory coding assignment in the USN course for Python introduction
# Author Anders Bakken / bakken.anders@gmail.com
# Taking age as input and calculate how many pizzaz you would need to purchase based on people eating 1/4 each

import math

class Oppg_5():
    def __init__(self):
        pass
    
    def run(self):
        try:
            while True:
                self.callUser()
                user_input = input("Enter value: ")
                user_input = int(user_input)
                if not (1 <= user_input <= 2):
                    print("Invalid input. Exiting")
                    break
                if user_input == 1:
                    self.calculate()
                elif user_input == 2:
                    break
        except Exception as e:
            print(f"An error occured: {e}")
    
    #Ask for user for lookup in the dataset or add to the dataset
    def callUser(self):
        """
        Prompts the user with options to either continiue the calculations or exit the program.

        Options:
        1. New calculation
        2. Exit program
        """
        
        print("\nDo you want to do calculations: Press 1")
        print("Do you want to exit: Press 2")
        print("Any other values will exit the program")
    
    def calculate(self):
        try:
            diameter = float(input("Enter the length of the diameter: "))
            leg_triangel = float(input("Enter the length of the side of the triangle: "))
            totalt_area, circumference = self.doCalculation(diameter, leg_triangel)
            
            print(f"The area of the figure is: {totalt_area:.2f}")
            print(f"The outer perimeter is: {circumference:.2f}")
        except ValueError:
            print("Invalid input. Please enter a valid number")
        except Exception as e:
            print(f"An error occured: {e}")
            
    def doCalculation(self, a: float, b: float):
        """
        Calculate the area and outer perimeter of a figure.
        Given a figure where input are the legs of a tirangle with a semicircle on top
        The semicircle are located on the short leg of the figure
        Input a are also the diameter of the circle
        Input parameters:
        a : float : The length of the diameter
        b : float : The length of the side of the triangle
        """      
        # Radius of the circle
        r = a / 2
        
        # Calculate the hypotenuse
        hypotenuse = math.sqrt(b**2 + a**2)
        
        # Area of ​​the triangle
        area_triangle = (a * b) / 2
        
        # Area of ​​the circle
        area_circle = (math.pi * r**2) / 2
        
        # Totalt area
        totalt_area = area_triangle + area_circle
        
        # Outer circumference = a + b + arc of the semicircle
        circumference = b + hypotenuse + (math.pi * r)
        
        return totalt_area, circumference
           
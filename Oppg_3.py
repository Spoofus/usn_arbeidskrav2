#!/usr/bin/env
# Second mandatory coding assignment in the USN course for Python introduction
# Author Anders Bakken / bakken.anders@gmail.com
# Taking age as input and calculate how many pizzaz you would need to purchase based on people eating 1/4 each

import numpy as np

class Oppg_3():
    def __init__(self):
        v_grad = 0
    
    def convertToRadians(self, v_grad):
        """ Function to convert degrees to radians. 
        Neat trick would be to use build in function in numpy package to convert np.radians(v_grad)
        But we do it manually"""
        return v_grad * np.pi / 180
    
    
    def run(self):
        """ Main function for the class and acting as a controller. """
        try:
            v_grad = float(input('Skriv inn grader du ønsker å konvertere: '))
            v_rad = self.convertToRadians(v_grad)
            print("The Grade : {:.2f} as radians are : {:.4f}".format(v_grad, v_rad))
        except ValueError:
            print("Invalid input. Please enter a valid number as grades in Integer")

            
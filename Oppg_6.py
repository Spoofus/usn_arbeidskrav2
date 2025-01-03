#!/usr/bin/env
# Second mandatory coding assignment in the USN course for Python introduction
# Author Anders Bakken / bakken.anders@gmail.com
# Taking age as input and calculate how many pizzaz you would need to purchase based on people eating 1/4 each

import numpy as np
import matplotlib.pyplot as plt

class Oppg_6():
    def __init__(self):
        pass
    
    def run(self):
        # Generate 200 points evenly spaced between -10 and 10
        x = np.linspace(-10, 10, 200)

        # Calculate the corresponding y values
        y = self.f(x)

        # Plot the function
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Plot of f(x) = -x^2 - 5')
        plt.grid(True)
        plt.show()

    # Define the function f(x) = -x^2 - 5
    def f(self,x):
        return -x**2 - 5

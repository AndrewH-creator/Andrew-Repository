
"""
Program Name: Lab 4 - Plotting Cubic Numbers
Author: Andrew Hissong
Purpose: Generate two graphs showing the first 5 cubes
         and the first 5000 cubes using matplotlib.
Starter Code: No starter code used.
Date: November 17, 2026
"""

import matplotlib.pyplot as plt

# Part 1: First 5 Cubes
x_values = [1, 2, 3, 4, 5]
y_values = [1, 8, 27, 64, 125]

plt.figure()
plt.plot(x_values, y_values, color="blue", marker="o")
plt.title("First 5 Cubes")
plt.xlabel("Value")
plt.ylabel("Cube of Value")
plt.grid(True)
plt.savefig("cubes_5.png")
plt.close()

# Part 2: First 5000 Cubes
x_values = list(range(1, 5001))
y_values = [value ** 3 for value in x_values]

plt.figure()
plt.plot(x_values, y_values, color="green")
plt.title("First 5000 Cubes")
plt.xlabel("Value")
plt.ylabel("Cube of Value")
plt.grid(True)
plt.savefig("cubes_5000.png")
plt.close()

print("Both graphs have been created successfully!")

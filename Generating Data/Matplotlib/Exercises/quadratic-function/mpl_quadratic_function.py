import matplotlib.pyplot as plt
import numpy as np

# Define Quadratic function
def quadratic_function(x, a, b, c):
    return a * x**2 + b * x + c

a = int(input("Enter value of a: "))
b = int(input("Enter value of c: "))
c = int(input("Enter value of c: "))

x_values = np.linspace(-10, 10, 40)
y_values = quadratic_function(x_values, a, b, c)

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

# Set chart title and labels axes
ax.set_title("Quadratic function", fontsize=24)
ax.set_xlabel("x", fontsize=14)
ax.set_ylabel("y", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14)
ax.grid(True)

plt.show()






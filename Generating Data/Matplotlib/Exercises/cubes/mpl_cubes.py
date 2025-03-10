import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]




fig, ax = plt.subplots()
ax.plot(x_values, y_values ,linewidth=3)

# Set chart title and label axes
ax.set_title("cubes Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Values", fontsize=14)

# Set size of tick labels.rrrrrrrrrrrrr
ax.tick_params(axis='both', labelsize=14)

ax.grid()

plt.show()
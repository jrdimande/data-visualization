import matplotlib.pyplot as plt
def factorial(x):
    result = 1
    while x > 1:
        result *= x
        x -= 1
    return result

x_values = [x for x in range(1, 6)]
y_values = [factorial(x) for x in x_values]

plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(x_values, y_values, linewidth=3)
ax.grid(True)

# Set chart title and labels axes
ax.set_title("Factorial", fontsize=24)
ax.set_xlabel("X", fontsize=14)
ax.set_ylabel("Y", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14)



plt.show()


import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator, FuncFormatter

filename = '../../data/world_population.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get data from this file
    years, numbers = [], []
    for row in reader:
        # Check if country code == MOZ
        if row[1] == 'MOZ':
            num = int(row[3])
            year = int(row[2])
            numbers.append(num)
            years.append(year)

fig, ax = plt.subplots()
ax.scatter(years, numbers)

# Disable scientific notation
ax.yaxis.set_major_locator(MaxNLocator(integer=True))

def currency(x, pos):
    return f'{x:,.0f}'  # Format the number with commas

ax.yaxis.set_major_formatter(FuncFormatter(currency))


plt.show()

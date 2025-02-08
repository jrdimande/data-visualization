import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = '../../data/sanfrancisco-california.csv.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get highs and lows from this file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        try:
            high = int(row[2])
            low = int(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot the high and low temperatures
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5, label='High Temp')
ax.plot(dates, lows, c='blue', alpha=0.5, label='Low Temp')
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
ax.grid(True)
fig.autofmt_xdate()

# Set chart title and label axes
ax.set_title('Daily high and temperatures - 2024', fontsize=24)
ax.set_ylabel('Temperatures(F)')

# Set label size
ax.tick_params(axis='both', labelsize=16)
plt.legend(loc='upper left')
plt.show()

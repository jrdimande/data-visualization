import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = '../../data/sitka.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get high temperatures from this file
    dates, highs, lows = [], [], []
    for row in reader:
        concurrent_date = datetime.strptime(row[0], '%Y-%m-%d')
        high = int(row[2])
        low = int(row[3])
        dates.append(concurrent_date)
        highs.append(high)
        lows.append(low)
    print(highs)

# Plot the high temperatures
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5, linewidth=3)
ax.plot(dates, lows, c='blue', alpha=0.5, linewidth=3)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.5)
fig.autofmt_xdate()

# Format plot
ax.set_title("Daily high temperature, jan 2025", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

ax.grid()
plt.show()
fig.autofmt_xdate()


plt.show()
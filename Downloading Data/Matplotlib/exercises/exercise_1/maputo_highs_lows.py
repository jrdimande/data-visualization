import csv
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

filename = '../../data/67341099999.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get highs, lows and dates
    dates, lows, highs = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[1], '%Y-%m-%d')
        print(current_date)
        high = (float(row[20]) - 32 )* (5/9)
        low = (float(row[22]) - 32 )* (5/9)
        lows.append(low)
        highs.append(high)
        dates.append(current_date)


# Visualize
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates,highs, lows, facecolor='#ADD8E6', alpha=0.5)

# Set titles
ax.set_title('Daily high and low temperatures in Maputo-2024', fontsize=24)
ax.set_xlabel('Date', fontsize=16)
ax.set_ylabel('Temperatures(C')

ax.tick_params(axis='both', which='major', labelsize=16)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

fig.autofmt_xdate()
plt.show()





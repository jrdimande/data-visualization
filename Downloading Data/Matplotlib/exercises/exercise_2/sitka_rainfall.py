import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename ='../../data/sitka.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get the PRCP from this file
    dates, prcps = [], []
    for row in reader:
        prcp = float(row[4])
        prcps.append(prcp)
        date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(date)


# Visualize the results
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.plot(dates, prcps, c='blue')

    # Set chart title and labes axes
    ax.set_title('Sitka Rainfall', fontsize=24)
    ax.set_xlabel('Date', fontsize=14)
    ax.set_ylabel('PRCPS', fontsize=14)
    fig.autofmt_xdate()
    ax.grid(True)

    # Set size of tick labels
    ax.tick_params(axis='both', labelsize=14)

    plt.show()




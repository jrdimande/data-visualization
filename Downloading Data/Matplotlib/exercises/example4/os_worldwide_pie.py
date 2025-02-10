import csv
import matplotlib.pyplot as plt

filename = '../../data/os_combined-ww-monthly-202401-202501.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    rows, names, percentages = [], [], []
    # Get the rows.
    for row in reader:
        rows.append(row)

    # Get the OS name.
    for name in header_row:
        if name == 'Date':
            continue
        names.append(name)

    # Get the percentages
    for percentage in rows[0][1:]:
        percentages.append(int(float(percentage)))


# Plot the percentages of each OS
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_title("Desktop Operating Systems")

ax.pie(percentages, autopct='%1.1f%%' ,startangle=100)
# Create the legend
plt.legend(names, loc="center left", bbox_to_anchor=(1, 0.5))

plt.show()

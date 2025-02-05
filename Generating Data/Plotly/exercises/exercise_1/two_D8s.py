from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# Create  two eight
die_1 = Die()
die_2 = Die()


# Make some rolls,a and store results in a list
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)


# Analyze the results
frequencies = []
max_result = die_1.num_Sides + die_2.num_Sides
for value in range(4, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
x_values = list(range(4, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title' : 'Result', 'dtick' : 1 }
y_axis_config = {'title' : 'Frequency of Result'}
my_layout = Layout(title='Result of rolling two D6 dice 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data' : data, 'layout' : my_layout}, filename='d8_d8.html')


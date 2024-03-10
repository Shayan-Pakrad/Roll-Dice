import plotly.express as px   # Importing the plotly.express library for creating the plot

# Importing the Die class from the die module
from die import Die

# Creating a 6-sided die object
die_1 = Die()

# Creating a 10-sided die object
die_2 = Die(10)

# Initializing an empty list to store the results of rolling the two dice
results = []

# Running a loop 50,000 times, in each iteration rolling both dice and adding the results together.
# The total result is appended to the results list.
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Initializing an empty list to store the frequency of each possible result
frequencies = []

# Setting the maximum possible result to the sum of the number of sides of both dice
max_result = die_1.num_sides + die_2.num_sides

# Looping through all possible results (from 2 to the maximum possible result)
# and counting the number of times each result appears in the results list,
# storing the count in the frequencies list.
poss_result = range(2, max_result+1)
for value in poss_result:
    frequency = results.count(value)
    frequencies.append(frequency)

# Setting the plot title and labels for the x and y axes
title = "Results of Rolling a D6 and a D10 50,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}

# Creating a bar chart using plotly.express.bar(), passing in the possible results
# and their corresponding frequencies
fig = px.bar(x=poss_result, y=frequencies, title=title, labels=labels)

# Updating the layout of the chart to display the x-axis tick marks at intervals of 1
fig.update_layout(xaxis_dtick=1)

# Displaying the chart using fig.show()
fig.show()
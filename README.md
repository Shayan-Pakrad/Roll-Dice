
# Roll Dice

This Python script uses the Plotly library to create a histogram of the results of rolling two dice, a 6-sided die (D6) and a 10-sided die (D10), a total of 50,000 times.


## Prerequisites

- Python 3.x
- Plotly library
## Code Structure

1. Import the necessary libraries: plotly.express for creating the plot, and die (which is not included in the code snippet) for creating the dice objects.
2. Create two dice objects, die_1 and die_2, with die_1 being a 6-sided die and die_2 being a 10-sided die.
3. Initialize an empty list results to store the results of rolling the two dice.
4. Run a loop 50,000 times, in each iteration rolling both dice and adding the results together. The total result is appended to the results list.
5. Initialize an empty list frequencies to store the frequency of each possible result.
6. Set the maximum possible result to the sum of the number of sides of both dice.
7. Loop through all possible results (from 2 to the maximum possible result) and count the number of times each result appears in the results list, storing the count in the frequencies list.
8. Set the plot title and labels for the x and y axes.
9. Create a bar chart using plotly.express.bar(), passing in the possible results and their corresponding frequencies.
10. Update the layout of the chart to display the x-axis tick marks at intervals of 1.
11. Display the chart using fig.show().

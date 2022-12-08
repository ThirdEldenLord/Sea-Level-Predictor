import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter('Year', 'CSIRO Adjusted Sea Level', data = df, s = 15)

    # Create first line of best fit
    result = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    slope = result.slope
    intercept = result.intercept
    first_line_x = np.arange(df["Year"].min(), 2051)
    first_line_y = slope*first_line_x + intercept
    plt.plot(first_line_x, first_line_y, color = "red")

    # Create second line of best fit
    new_df = df[df["Year"] >= 2000]
    result = linregress(new_df["Year"], new_df["CSIRO Adjusted Sea Level"])
    slope = result.slope
    intercept = result.intercept
    second_line_x = np.arange(new_df["Year"].min(), 2051)
    second_line_y = slope*second_line_x + intercept
    plt.plot(second_line_x, second_line_y, color = "green")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
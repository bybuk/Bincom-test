import random
from statistics import mean, median, mode

import numpy as np

# List of colors
monday = ["GREEN","YELLOW","GREEN","BROWN","BLUE","PINK","BLUE","YELLOW","ORANGE","CREAM","ORANGE","RED","WHITE","BLUE",
          "WHITE","BLUE","BLUE","BLUE","GREEN"]
tuesday = ["ARSH","BROWN","GREEN","BROWN","BLUE","BLUE","BLEW","PINK","PINK","ORANGE","ORANGE","RED","WHITE","BLUE",
           "WHITE","WHITE","BLUE","BLUE","BLUE"]
wednesday = ["GREEN","YELLOW","GREEN","BROWN","BLUE","PINK","RED","YELLOW","ORANGE","RED","ORANGE","RED","BLUE","BLUE",
             "WHITE","BLUE","BLUE","WHITE","WHITE"]
thursday = ["BLUE","BLUE","GREEN","WHITE","BLUE","BROWN","PINK","YELLOW","ORANGE","CREAM","ORANGE","RED","WHITE","BLUE",
            "WHITE","BLUE","BLUE","BLUE","GREEN"]
friday = ["GREEN","WHITE","GREEN","BROWN","BLUE","BLUE","BLACK","WHITE","ORANGE","RED","RED","RED","WHITE","BLUE",
          "WHITE","BLUE","BLUE","BLUE","WHITE"]

colors = monday + tuesday + wednesday + thursday + friday

total_colors = len(colors)

def colors_frequency(colors_list: list[str]) -> dict[str, int]:
    color_frequency = {}

    for color in colors_list:
        if color in color_frequency:
            color_frequency[color] += 1
        else:
            color_frequency[color] = 1

    return color_frequency

# Calculate mean
def mean_of_colors()-> int:
    mean_color_length = mean(len(color) for color in colors)

    return mean_color_length

# Calculate median
def median_of_colors()-> int:
    median_color_length = median(len(color) for color in colors)

    return median_color_length

# Calculate mode
def mode_of_colors()-> int:
    mode_color = mode(colors)
    return mode_color

# Calculate variance
def variance_of_colors()-> int: 
    variance_color_length = np.var([len(color) for color in colors])

    return variance_color_length

# probability
def probability_of_red()-> int: 
    colors_dict = colors_frequency(colors)
    
    return colors_dict["RED"] / total_colors

def genRandomBinary()-> int: 
    binary_num = ''.join(str(random.randint(0, 1)) for _ in range(4))

    return binary_num


def toBaseTen(str_number: str)-> int: 
    # Convert binary number to base 10
    decimal_num = int(str_number, 2)

    return decimal_num

def fibonacci(number: int) -> int:
    a, b = 0, 1
    fib_sum = a + b
    for _ in range(2, number):
        a, b = b, a + b
        fib_sum += b
    return fib_sum



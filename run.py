
from main import *


def pick_options() -> str:
    return input(
"""
What would you like to do ?
1. See colors frequency
2. See full colors list
3. mean color
4. median color
5. probability of picking red color
6. variance of the colors
7. Save the colours and their frequencies in postgresql database
8. generates random 4 digits number of 0s and 1s and convert the generated number to base 10
9. sum the first 50 fibonacci sequence
"""
)

def runApp():
    option = int(pick_options())

    while option > 9 or option < 1:
        option = int(pick_options())
        
    if(option == 1):
        print(colors_frequency(colors))
    elif(option == 2):
        print(f"colors = {colors}")
    elif(option == 3):
        print(f"mean = {mean_of_colors()}")
    elif(option == 4):
        print(f"median = {median_of_colors()}")
    elif(option == 5):
        print(f"probability of red = {probability_of_red()}")
    elif(option == 6):
        print(f"variance of colors = {variance_of_colors()}")
    elif(option == 7):
        print("Data saved to DB")
    elif(option == 8):
        binary = genRandomBinary()
        base_10 = toBaseTen(binary)
        print(f"""
Random binary = {binary}
Base10 Equivalent = {base_10}
            """)
    elif(option == 9):
        print(f"The sum of first 50 fibonacci sequence = {fibonacci(50)}")
    else:
        print("unknown option selected")


runApp()
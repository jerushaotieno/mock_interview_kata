# QUESTION

# In this little assignment you are given a string of space separated numbers, and have to return 
# the highest and lowest number.

# Examples
# highAndLow("1 2 3 4 5");  // return "5 1"
# highAndLow("1 2 -3 4 5"); // return "5 -3"
# highAndLow("1 9 3 4 -5"); // return "9 -5"
# Notes
# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.


# PSEUDOCODE

# Define your function
# Split the string and make it a list  
# Let i = 0
# Create a while loop
# Check the highest and lowest number if set condition is true
# Run and return your value in the terminal

# CODE

def highAndLow(numbers):
    # split string by space character
    numberList = numbers.split(" ")
    i = 0
    lowest = int(numberList[0])
    highest = int(numberList[0])

    while i < len(numberList):
        numberList[i] = int(numberList[i])
        if numberList[i] < lowest:
            lowest = numberList[i]
        if numberList[i] > highest:
            highest = numberList[i]
        i += 1

    x = highest+" "+lowest
    return str(x)

  










def highAndLow(numbers): 
    # split string by space character
    numbers = numbers.split(" ")
    # convert string array to int, also making list from them
    numbers = list(map(int, numbers))
    return max(numbers), min(numbers)

print(highAndLow("1 2 3 4 5"))
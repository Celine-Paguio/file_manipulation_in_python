# This program will read a text file named "numbers.txt" and will categorize the numbers as odd or even. After categorizing, it will get the square of even integers then write it in double.txt then get the cube of odd integers and write it in triple.txt. 

# Start of program
# Read integers.txt file
with open("integers.txt", "r") as integers_file:
    integers = integers_file.read().splitlines()
    print(integers)
# Convert string to integer
# Categorize the integers to even or odd
# Write even numbers to even.txt
# Write odd numbers to odd.txt
# Determine the square of even numbers
# Determine the cube of odd numbers
# Write the square of even numbers to double.txt
# Write the cube of odd numbers to triple.txt
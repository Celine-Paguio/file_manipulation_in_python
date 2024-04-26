# This program will read a text file named "numbers.txt" and will categorize the numbers as odd or even

# Start of program
# Read numbers.txt file
with open("numbers.txt", 'r') as numbers_file:
    numbers = numbers_file.read().splitlines()
# Convert string to integers
    numbers = [int(num) for num in numbers]
    print(numbers)
# Categorize the numbers as even or odd
# Write even numbers to even.txt
# Write odd numbers to odd.txt
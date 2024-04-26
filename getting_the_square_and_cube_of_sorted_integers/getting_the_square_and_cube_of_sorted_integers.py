# This program will read a text file named "numbers.txt" and will categorize the numbers as odd or even. After categorizing, it will get the square of even integers then write it in double.txt then get the cube of odd integers and write it in triple.txt. 

# Start of program
# Read integers.txt file
with open("integers.txt", "r") as integers_file:
    integers = integers_file.read().splitlines()
# Convert string to integer
    integers = [int(num) for num in integers]
# Categorize the integers to even or odd
# Write even numbers to even.txt
with open("even.txt", "a") as even_file:
    for num in integers:
        if num %2 == 0:
            even_numbers = num
            even_file.write(str(even_numbers) + "\n")
        else:
            odd_numbers = num
# Write odd numbers to odd.txt
# Determine the square of even numbers
# Determine the cube of odd numbers
# Write the square of even numbers to double.txt
# Write the cube of odd numbers to triple.txt
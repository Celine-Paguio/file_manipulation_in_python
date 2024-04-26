# This program will read a text file named "numbers.txt" and will categorize the numbers as odd or even

# Start of program
# Read numbers.txt file
with open("numbers.txt", 'r') as numbers_file:
    numbers = numbers_file.read().splitlines()
# Convert string to integers
    numbers = [int(num) for num in numbers]

# Categorize the numbers as even or odd
# Write even numbers to even.txt
with open("even.txt", "a") as even_file:
    for num in numbers:
        if num %2 == 0:
            even_numbers = num
            even_file.write(str(even_numbers) + "\n")
        else:
            odd_numbers = num
# Write odd numbers to odd.txt
            with open("odd.txt", "a") as odd_file:
                odd_file.write(str(odd_numbers)+"\n")
# Print a message to notify the user that the program is done
print ('Even and odd numbers from "numbers.txt" have been sorted. You can check "even.txt" and "odd.txt" for the results.')

# End of program
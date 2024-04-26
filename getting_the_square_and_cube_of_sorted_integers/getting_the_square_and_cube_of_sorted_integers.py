# This program will read a text file named "numbers.txt" and will categorize the numbers as odd or even. After categorizing, it will get the square of even integers then write it in double.txt then get the cube of odd integers and write it in triple.txt. 

# Start of program
# Read integers.txt file
with open("integers.txt", "r") as integers_file:
    integers = integers_file.read().splitlines()
# Convert string to integer
    integers = [int(num) for num in integers]
# Categorize the integers to even or odd
# Write even integers to even.txt
with open("even.txt", "a") as even_file:
    for num in integers:
        if num %2 == 0:
            even_integers = num
# Determine the square of even integers
            square_of_even = (even_integers ** 2)
            # print(square_of_even)
            even_file.write(str(even_integers) + "\n")
        else:
            odd_integers = num
# Determine the cube of odd integers
            cube_of_odd = (odd_integers ** 3)
            print(cube_of_odd)
# Write odd integers to odd.txt
            with open("odd.txt", "a") as odd_file:
                odd_file.write(str(odd_integers)+"\n")

# Write the square of even integers to double.txt
# Write the cube of odd integers to triple.txt
# This program will prompt the user to input texts then write the text contents into my_file.txt

# Start of program
# Create a file named my_file.txt
with open("my_file.txt", "w") as my_file:
# Ask the user for input
    line = input("Enter line: ")
    my_file.write(line + "\n")
# Ask the user if they want to add more lines
# Print a message once the user don't want to add more lines or if they entered an incorrect key
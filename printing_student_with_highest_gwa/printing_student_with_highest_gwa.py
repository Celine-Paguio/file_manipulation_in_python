# This program will read a binary file containing students name and their GWA and print the name of the student with the highest GWA including his/her GWA.

# Import the pickle module to read binary file 
import pickle
# Read the binary file
with open("students.bin", "rb") as file:
# Load the students dictionary
    students = pickle.load(file)
    print(students)
# Determine the student with the highest GWA
# Print the student with the highest GWA
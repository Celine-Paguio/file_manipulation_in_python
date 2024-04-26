# This program will read a binary file containing students name and their GWA and print the name of the student with the highest GWA including his/her GWA.

# Import the pickle module to read binary file 
import pickle
# Read the binary file
with open("students.bin", "rb") as file:
# Load the students dictionary
    students = pickle.load(file)
# Determine the student with the highest GWA
highest_student = min(students, key=students.get)
# Determine the GWA of the highest student
highest_gwa = students[highest_student]
print(highest_gwa)
# Print the student with the highest GWA
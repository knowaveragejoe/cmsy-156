# CMSY-156
# Programmer name: Joseph Clark 
# 02/27/22 
# Lab 6: Files part 2

# Take user input for filename one and attempt to read it
while True:
    filename_one = input("Enter the path and name of the first file: ")
    try:
        file_one = open(filename_one, "r")
        break
    except:
        print("File not found or could not be opened. Try again")

# Take user input for filename two and attempt to read it
while True:
    filename_two = input("Enter the path and name of the second file: ")
    try:
        file_two = open(filename_two, "r")
        break
    except:
        print("File not found or could not be opened. Try again")

# Take user input for the output filename and try to open it for writing
while True:
    output_filename = input("Enter the path and name of the output file: ")
    try:
        output_filename = open(output_filename, "w")
        break
    except:
        print("File not found or could not be opened. Try again")

print("Name processing started.")

# Read the first file using a while loop and write to output file
file_one_data = file_one.readline()
while file_one_data != "":
    output_filename.write(file_one_data)
    file_one_data = file_one.readline()

# Read the second file using a for loop and write to output file
for line_two_data in file_two:
    output_filename.write(line_two_data) 

# Close all files
file_one.close()
file_two.close()
output_filename.close()

print("Name processing complete.")
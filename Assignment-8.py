# Ask the user for the input file path
input_file = input("Enter the full path of the input text file: ").strip('"')

# Read data from the input file
with open(input_file, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Count the total number of lines
print("Total number of lines:", len(lines))

# Extract the first two lines
first_two_lines = lines[:2]

# Create the output file
output_file = "output.txt"

# Write the first two lines into the output file
with open(output_file, "w", encoding="utf-8") as file:
    file.writelines(first_two_lines)

print("First two lines have been written to output.txt")


# ---------------- OUTPUT ----------------
# Enter the full path of the input text file: "C:\Users\Admin\Desktop\input.txt.txt"
# Total number of lines: 4
# First two lines have been written to output.txt
#
# Contents of output.txt:
# Hello, this is line one.
# This is line two.
# -----------------------------------------

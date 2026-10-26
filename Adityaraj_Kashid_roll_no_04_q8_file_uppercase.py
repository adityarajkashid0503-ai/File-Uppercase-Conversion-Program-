"""
Q8. Develop a Python program to read a text file and write its contents
into another file after converting the text.

Input file  : input.txt
Output file : output.txt
"""
import os

# Create sample input.txt if it does not already exist
if not os.path.exists("input.txt"):
    with open("input.txt", "w") as f:
        f.write("python programming\n"
                "file handling is useful\n"
                "regular expressions are important.")

try:
    # Read the input file
    with open("input.txt", "r") as infile:
        content = infile.read()

    # Convert: first letter of each line in capital (matches expected output)
    converted = "\n".join(line.capitalize() for line in content.split("\n"))

    # For full upper case instead, use this line:
    # converted = content.upper()

    # Write to the output file
    with open("output.txt", "w") as outfile:
        outfile.write(converted)

    print("File converted successfully!\n")

    # Show the output file contents
    with open("output.txt", "r") as f:
        print("Contents of output.txt:")
        print(f.read())

except FileNotFoundError:
    print("Error: input.txt not found.")

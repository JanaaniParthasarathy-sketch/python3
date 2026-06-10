# File Handling & Working with External Data

# Writing data to a file
file = open("data.txt", "w")
file.write("Name: Janaani\n")
file.write("Course: AI & Data Science\n")
file.write("College: HITS Chennai\n")
file.close()

print("Data written successfully!\n")

# Reading data from the file
file = open("data.txt", "r")
content = file.read()
print("File Content:")
print(content)
file.close()

# Appending new data
file = open("data.txt", "a")
file.write("Internship: Python Programming\n")
file.close()

print("\nData appended successfully!\n")

# Reading updated content
file = open("data.txt", "r")
updated_content = file.read()
print("Updated File Content:")
print(updated_content)
file.close()

# Import json package to read JSON files
import json

# Get user input for which json file to open
file = input("Enter the JSON filename\n")
print('Opening ' + file + '...\n')

# Open JSON File
f = open(file,"r",encoding='utf-8')


# Returns JSON object as dictionary
data = json.load(f)

# Prints the JSON list
for i in data["CVE_Items"]:
    print(i + "\n")

# Close file
f.close
# Import json package to read JSON files
import json

# Get user input for which json file to open
while True:
    file = input("Enter the JSON filename\n")
    print('\nOpening ' + file + '...\n')
    try:
        f = open(file,"r",encoding='utf-8')
        break
    except IOError:
        input("Error in file opening, press Enter to enter filename again\n")

# Returns JSON object as dictionary
data = json.load(f)
cves = data["CVE_Items"]

# 'i' here is each cve key value
# description values is this path "cves[ind]['cve']['description']['description_data'][0]['value']"
ind = 0
count = 0

newJson = json.dumps(cves, indent = 4)
# print(newJson)

# Words to search for in description
substrings = ['XSS', 'xss', 'cross site scripting', 'cross-site scripting']

foundCVE = {}

for i in cves:
    CVE_id = cves[ind]['cve']['CVE_data_meta']['ID']
    description = cves[ind]['cve']['description']['description_data'][0]['value']
    if any(word in description for word in substrings):
        foundCVE[CVE_id] = description
        count = count + 1
        print('\n')
    ind = ind + 1

print("There are " + str(count) + " description(s) with xss in them")

with open('foundCVEs', 'w') as convert_file:
    convert_file.write(json.dumps(foundCVE, indent=4))

# Prints the JSON list
# searching = input("Enter data parameter you want to search for\n")
# if searching in cves:
#     print(cves[searching])
# else:
#     print("Parameter is not present")

# Close file
f.close
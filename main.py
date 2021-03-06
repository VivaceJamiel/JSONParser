# Import json package to read JSON files
import json

def showList(list):
    for x in list:
        print(x.CVEID)
        print(x.description)
        if x.impact:
            print(x.impact)
        else:
            print("No Impact")


class CVE:
    def __init__(self, CVEID, description, impact):
        self.CVEID = CVEID
        self.description = description
        self.impact = impact




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
substrings = ['XSS', 'xss', 'cross site scripting', 'cross-site scripting', 'sql injection', 'SQL injection']

CVEDescriptions = {}
fullCVE = {}
CVEList = []

# Goes through each cve in zip file and saves them into files if they have substring
for i in cves:
    CVE_id = cves[ind]['cve']['CVE_data_meta']['ID']
    description = cves[ind]['cve']['description']['description_data'][0]['value']
    impact = cves[ind]['impact']

    if any(word in description for word in substrings):
        temp = CVE(CVE_id, description, impact)
        CVEDescriptions[CVE_id] = description
        fullCVE[CVE_id] = i
        CVEList.append(temp)
        count = count + 1
    ind = ind + 1

print("There are " + str(count) + " description(s) with key words in them")

# Writes to file with 
with open('foundCVEDescriptions', 'w', encoding="utf-8") as convert_file:
    convert_file.write(json.dumps(CVEDescriptions, indent=4))

with open('foundCVEFull', 'w', encoding="utf-8") as convert_file:
    convert_file.write(json.dumps(fullCVE, indent=4))

with open('CVEList', 'w', encoding="utf-8") as convert_file:
    for element in CVEList:
        convert_file.write(element.CVEID + "\n" + element.description + "\n" + json.dumps(element.impact) + "\n")
convert_file.close()

# showList(CVEList)

f.close
import json

# Open the first JSON file
with open('file1.json', 'r') as file1:
    data1 = json.load(file1)

# Open the second JSON file
with open('file2.json', 'r') as file2:
    data2 = json.load(file2)

# Append the second file to the first
data1.extend(data2)

# Write the combined data to a new file
with open('combined_file.json', 'w') as outfile:
    json.dump(data1, outfile)

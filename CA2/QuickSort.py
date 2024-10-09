import json

# Read the data from the JSON file
with open('integer_data.json', 'r') as file:
    data = json.load(file)

#---------------------------Verify the generated Data---------------------------------------#
# Output the first group (to avoid printing a large amount of data)
# print(data[0][0][0])

for j in range(10):
    print("Group ", j)
    for i in range(8):
        print("Array", i,len(data[j][i]))

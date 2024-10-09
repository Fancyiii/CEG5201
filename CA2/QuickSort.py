import json

# Read the data from the JSON file
with open('integer_data.json', 'r') as file:
    data = json.load(file)

# #------------------------------------------------------------------#
# # Uncomment this section to Verify the generated Data
# # Output the first group (to avoid printing a large amount of data)
# print(data[0][0])

# for j in range(10):
#     print("Group ", j)
#     for i in range(8):
#         print("Array", i,len(data[j][i]))
# #------------------------------------------------------------------#

target_array = data[0][0]

def partition(A, lo, hi):
    pivot = A[lo]
    i = lo - 1
    j = h + 1

    while()



def quicksort(A, lo, hi):
    if target_array[lo]>= 0 and target_array[hi]>=0 and target_array[lo] < target_array[hi]:
        p = partition(A, lo, hi)
        quicksort(A, lo, hi)
        quicksort(A, p + 1, hi)



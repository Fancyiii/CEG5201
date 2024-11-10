import json
import time

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

def partition(A, lo, hi):
    pivot = A[lo]
    i = lo
    j = hi

    while(1):
        while(i < hi and A[i] < pivot):
            i += 1
        while(j > lo and A[j] >= pivot):
            j -= 1
        if i >= j:
            return j
        A[j], A[i] = A[i], A[j] #swap A[i] and A[j]

def quickSort(A, lo, hi):
    if lo >= 0 and hi >= 0 and lo < hi:
        p = partition(A, lo, hi)
        quickSort(A, lo, p)
        quickSort(A, p + 1, hi)

# Verify the sorted array
def verify(A):
    for i in range(0, len(A)):
        for j in range(i, len(A)):
            if A[i] > A[j]:
                return False
    return True
        

if __name__ == "__main__":
    GroupT = []
    for j in range(0, 10):
        T = []
        for arr in data[j]:
            n = len(arr)
            start_time = time.time()
            quickSort(arr, 0, n - 1)
            T.append(time.time() - start_time)
        GroupT.append(T)
    print(GroupT)




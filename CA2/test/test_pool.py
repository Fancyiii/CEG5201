import multiprocessing
import time

# Modify the quicksort function to not create processes itself
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

def parallel_quicksort(arr):




    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]

    A = [[1,4,7], [13, 15, 10, 16], [29, 24, 25, 23, 22], [33, 35]]
    # Use the top-level Pool for parallel sorting

    start_time = time.time()
    with multiprocessing.Pool(processes=8) as pool:
        first, second, third, fourth = pool.map(quicksort, A)
    end_time = time.time()
    print(end_time-start_time)

    B = [[1,4,7], [13, 15, 10, 16], [29, 24, 25, 23, 22], [33, 35]]
    start_time = time.time()
    with multiprocessing.Pool(processes=2) as pool:
        first, second, third, fourth = pool.map(quicksort, B)
    end_time = time.time()
    print(end_time-start_time)

    print(first + second + third + fourth)
    return first + second + third + fourth
 
if __name__ == "__main__":
    array = [3, 6, 8, 10, 1, 2, 1, 5, 4, 9, 7]
    sorted_array = parallel_quicksort(array)
    print("Sorted array:", sorted_array)

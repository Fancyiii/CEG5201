import multiprocessing
import numpy as np
import pandas as pd
import time

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
    return A
    
def quickSortSeq_twoProc(A):

    lowerHalf = [x for x in A if x <= A[0]]
    upperHalf = [x for x in A if x > A[0]]

    with multiprocessing.Pool(processes=2) as pool:
        args = [(lowerHalf, 0, len(lowerHalf)-1), (upperHalf, 0, len(upperHalf)-1)]
        sortedLoerHalf, sortedUpperHalf = pool.starmap(quickSort, args)
    return sortedLoerHalf + sortedUpperHalf


if __name__ == "__main__":
    num_cores = multiprocessing.cpu_count()
    print(f"Number of CPU cores: {num_cores}")

    # Calculate time taken for arrays in group 0
    df = pd.read_csv("group_0.csv")
    print("\nSorting times for each array in group 0:")
    for column in df.columns:
        array = df[column].dropna().tolist()

        start_time = time.time()
        sorted_array = quickSortSeq_twoProc(array)
        end_time = time.time()

        print(f"Array {column}: {end_time - start_time:.6f} seconds")


    # Calculate time taken for each group
    group_sorting_times = []
    for group_num in range(10):

        df = pd.read_csv(f"group_{group_num}.csv")
        array_sorting_times = []
        group_start_time = time.time()
        for column in df.columns:
            array = df[column].dropna().tolist()  # Remove NaN values

            start_time = time.time()
            sorted_array = quickSortSeq_twoProc(array)
            end_time = time.time()

            array_sorting_times.append((column, end_time - start_time))
            # print(f"Sorting time for group {group_num}, array {column}: {end_time - start_time:.6f} seconds")

        group_end_time = time.time()
        group_sorting_times.append((group_num, group_end_time - group_start_time))
        # print(f"Total sorting time for group {group_num}: {group_end_time - group_start_time:.6f} seconds")

    print("\nSorting times for each group:")
    for group_num, time_taken in group_sorting_times:
        print(f"Group {group_num}: {time_taken:.6f} seconds")


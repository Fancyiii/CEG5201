import multiprocessing
import numpy as np
import pandas as pd
import time
import os
import random

def partition(A, lo, hi):
    pivot = A[random.randint(lo,hi)]
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

def partition_by_pivot(A, lo, hi, pivot):
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
    

def quickSortWrapper(arr):
    process_name = multiprocessing.current_process().name
    print(process_name)
    return quickSort(arr, 0, len(arr)-1)

# split data into several parts based on the number of processor and 
def split(A):
    with multiprocessing.Pool(processes=2) as pool:
        firstPivotPos, SecondPivotPos = pool.map(partition, [(A[0:len(arr)/2], arr[0]), (A[len(arr)/2+1 : len(arr)-1], arr[0])])
    return arr


def quickSortPal_twoProc(A):

    lowerHalf = [x for x in A if x <= A[0]]
    upperHalf = [x for x in A if x > A[0]]

    with multiprocessing.Pool(processes=8) as pool:
        sortedLowerHalf, sortedUpperHalf = pool.map(quickSortWrapper, [lowerHalf, upperHalf])
    return sortedLowerHalf + sortedUpperHalf

def quickSortPal_fourProc(A):

    lowerHalf = [x for x in A if x <= A[0]]
    upperHalf = [x for x in A if x > A[0]]

    Firstquarter  = [x for x in lowerHalf if x <= lowerHalf[0]]
    Secondquarter = [x for x in lowerHalf if x > lowerHalf[0]]
    Thirdquarter  = [x for x in upperHalf if x <= upperHalf[0]]
    Fourthquarter = [x for x in upperHalf if x > upperHalf[0]]

    # map_time_2proc_initial = time.time()
    # print(map_time_2proc_initial)
    with multiprocessing.Pool(processes=4) as pool:
        sortedFirstquarter, sortedSecondquarter, sortedThirdquarter, sortedFourthquarter = pool.map(quickSortWrapper, [Firstquarter, Secondquarter, Thirdquarter, Fourthquarter])
    return sortedFirstquarter + sortedSecondquarter + sortedThirdquarter + sortedFourthquarter

def quickSortPal_eightProc(A):

    lowerHalf = [x for x in A if x <= A[0]]
    upperHalf = [x for x in A if x > A[0]]

    Firstquarter  = [x for x in lowerHalf if x <= lowerHalf[0]]
    Secondquarter = [x for x in lowerHalf if x > lowerHalf[0]]
    Thirdquarter  = [x for x in upperHalf if x <= upperHalf[0]]
    Fourthquarter = [x for x in upperHalf if x > upperHalf[0]]

    FirstofEight = [x for x in Firstquarter if x <= Firstquarter[0]]
    SecondofEight = [x for x in Firstquarter if x > Firstquarter[0]]
    ThirdofEight = [x for x in Secondquarter if x <= Secondquarter[0]]
    FourthofEight = [x for x in Secondquarter if x > Secondquarter[0]]
    FifthofEight = [x for x in Thirdquarter if x <= Thirdquarter[0]]
    SixthofEight = [x for x in Thirdquarter if x > Thirdquarter[0]]
    SeventhofEight = [x for x in Fourthquarter if x <= Fourthquarter[0]]
    EighthofEight = [x for x in Fourthquarter if x > Fourthquarter[0]]

    with multiprocessing.Pool(processes=8) as pool:
        sortedFirst, sortedSecond, sortedThird, sortedFourth, sortedFifth, sortedSixth, sortedSeventh, sortedEighth = pool.map(quickSortWrapper, [FirstofEight, SecondofEight, ThirdofEight, FourthofEight, FifthofEight, SixthofEight, SeventhofEight, EighthofEight])
    return sortedFirst + sortedSecond + sortedThird + sortedFourth + sortedFifth + sortedSixth + sortedSeventh + sortedEighth

if __name__ == "__main__":
    num_cores = multiprocessing.cpu_count()
    print(f"Number of CPU cores: {num_cores} {os.cpu_count()}")

    # Calculate time taken for arrays in group 0
    df = pd.read_csv("group_0.csv")
    print("\nSorting times for each array in group 0:")
    for column in df.columns:
        array = df[column].dropna().tolist()

        start_time = time.time()
        sorted_array = quickSortPal_twoProc(array)
        # sorted_array = quickSortPal_fourProc(array)
        # sorted_array = quickSortPal_eightProc(array)
        end_time = time.time()

        print(f"Array {column}: {end_time - start_time:.6f} seconds")

    # # Calculate time taken for each group
    # group_sorting_times = []
    # for group_num in range(10):
    #     df = pd.read_csv(f"group_{group_num}.csv")
    #     array_sorting_times = []
    #     group_start_time = time.time()
    #     for column in df.columns:
    #         array = df[column].dropna().tolist()

    #         start_time = time.time()
    #         # sorted_array = quickSortPal_twoProc(array)
    #         # sorted_array = quickSortPal_fourProc(array)
    #         sorted_array = quickSortPal_eightProc(array)
    #         end_time = time.time()

    #         array_sorting_times.append((column, end_time - start_time))
    #         # print(f"Sorting time for group {group_num}, array {column}: {end_time - start_time:.6f} seconds")

    #     group_end_time = time.time()
    #     group_sorting_times.append((group_num, group_end_time - group_start_time))
    #     # print(f"Total sorting time for group {group_num}: {group_end_time - group_start_time:.6f} seconds")

    # print("\nSorting times for each group:")
    # for group_num, time_taken in group_sorting_times:
    #     print(f"Group {group_num}: {time_taken:.6f} seconds")


def arr_test(A):
    A[0], A[1] = A[1], A[0]

myA = [1, 2, 3, 4]
arr_test(myA)
print(myA)

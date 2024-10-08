import numpy as np

# Define matrices
A = np.array([  [  77,  -36,   54,  -72,   77,  -36,   54,  -72,       1,   92,  100,  -23,   93,  -44,   83,  -21],
                [  96,  -26,   29, - 93,   96,  -26,   29,  -93,      72,    2, -123,  126,  -72,  -10, -100,   11]])

B = np.array([  [ 114,  -46,  114,   27,  -37,  -19, -126,   34,    -100,   47,  -30,   55,   32,  125, -122,   89],
                [ 125,  -39,  -19,   63,   -7,  114,   46,    0,    -113,  -22,   74,  126,   18,  -11,  -17,   13],
                [  82, -118,   57, -127,  -48,   34,  -45,  -74,    - 72,  109,  -98,   20,   68, -106,   88,  -52],
                [ 108, -117, -101,  -93,   56, -105,   31,  -83,       4,  -17,  -68, -102,  111, -123,  -37,  125],
                [ -28,  -57, -127,   92,  -47,  -13,  108,  -18,     -65,   -7,  -98,  -50,  -39,   39,  -57,   70],
                [  13,  -16,  -73,   39,   72,  102,   67,  121,     -67,   84,  -49,   95,  -99,   81,   54,  -56],
                [-124,    4,  -91,   24, -123, -114,  -40,   66,     -36,   44,  -75,  -79, -115,  -39, -115,  -59],
                [  68,   -7, -122,  111,  -89,  -99,  -73,   54,     118,   92,  107,   88,  -11,  -21,  112,  -35],


                [ -95,   87,  -92,   41,   46,  118,   30, -114,      98,  -67,  -61,   18,  125,   48,  -88, -118],
                [  31,   26,  -19,   94,  119,  -65,  -81,  -32,     125,   13,  -20,   -7,   66,  108,  -61,  108],
                [  79,  -25,   16,   66,  -71, -119,  -17,  -32,     100,   59, -120, -101,   80,  -94,  -14,  -35],
                [ -98,  -93,   76,  122,   79,  -64,   13,   25,    -124,   31,   68,   25, -101,   29,  102,  -88],
                [   7,   87,   37,   61,  105,  -81,  105,   59,     -70,   92,   26,  -92,  -23,  -97, -123,   -2],
                [  76,  -67,  117,  116,  -28,   79,   82,   27,    -119,  -41,  -31, -112,  -97, -124,   52,  -94],
                [  39,  115,   54,    8,   70,  -43,   39,   24,      36,   82, -109, -112, -117, -115,   -9,   87],
                [  95,   27,   63,  -46, -122,   -5,   94,  111,     124,   66,   -1, -117,   12,  114,  -68, -122]])


# Splitting the original matrix into four 8x8 matrices using numpy


matrixA_1 = A[0:,:8]
matrixA_2 = A[0:,8:]

print(matrixA_1)
print(matrixA_2)

print("--------------------------")


matrix1 = B[:8, :8]
matrix2 = B[:8, 8:]
matrix3 = B[8:, :8]
matrix4 = B[8:, 8:]


print(matrix1)
print(matrix2)
print(matrix3)
print(matrix4)


# Matrix multiplication using NumPy's dot function
result = np.dot(A, B)

result1 = np.dot(matrixA_1,matrix1)
result2 = np.dot(matrixA_1,matrix2)
result3 = np.dot(matrixA_2,matrix3)
result4 = np.dot(matrixA_2,matrix4)

result_all_1 = result1 + result3

result_all_2 = result2 + result4



# vector = np.array([-128,  -91,   10,  -89,   10,   10,  127,   10])

# Add the vector to the result
# sum_result = result + vector

print("Matrix multiplication result:")
print(result)
print("------------------------")
print(result_all_1)
print(result_all_2)


# print("Sum with vector:")
# print(sum_result)
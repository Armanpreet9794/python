import numpy as np
# #ques 1
# d=np.arange(5,25)
# print ("d=",d)
# print(d.shape)
# print(d.ndim)
# print(d.dtype)

# #ques 2
# e=np.random.randint(10,50,size=(3,4))
# print("e-",e)
# print(e.shape)
# print(e.ndim)
# print(e.dtype)

# #ques 3
# a=np.array([2,4,6,8,10])
# b=np.array([1,3,5,7,9])
# sum=a+b
# print("addtion", sum)
# sub=a-b
# print("subtraction", sub)
# mult=a*b
# print("multiplication", mult)
# div=a/b
# print("division", div)

# #ques 4
# a=np.arange(1,10).reshape(3,3)
# print(a)
# mult=a*5
# print("multiplied by 5", mult)

#ques 5
# a=np.array(10,26),reshape(4,4)
# print(a)
# print("extract 2nd row",a[1])
# print("extract last row",a[2])

# # ques 6
# a=np.random.randint(20,40,size=10)
# print(a)
# ans=a>30
# print(ans)
# a=a[ans]
# print(a)

# #ques 7
# a=np.arange(11,24,size=12)
# print(a)
# b=np.a.reshape(3,4)
# print(b)

# #ques8
matrix_a=np.array([[1,2],[3,4]])
matrix_b=np.array([[1,2],[3,4]])
print("Matrix A:\n", matrix_a)
print("Matrix B:\n", matrix_b)
# Matrix Multiplication
matrix_product = np.dot(matrix_a, matrix_b)
print("Matrix Multiplication (A × B):\n", matrix_product)
# Transpose of Matrix A
transpose_A = matrix_a.T
print("Transpose of Matrix A:\n", transpose_A)

# # Ques 9 
# 9.1 
array_1d = np.random.randint(10, 61, size=15)
print("1D Array:", array_1d)
# 9.2
# Mean
mean_value = np.mean(array_1d)
print("Mean:", mean_value)
# Median
median_value = np.median(array_1d)
print("Median:", median_value)
# Standard Deviation
std_dev = np.std(array_1d)
print("Standard Deviation:", std_dev)


# # Ques 10 
# 10.1
A = np.array([[2, 1, 3], [0, 5, 6],[7, 8, 9]])

print("Matrix A:\n", A)
# 10.2
det_A = np.linalg.det(A)
print("Determinant of A:", det_A)
inverse_A = np.linalg.inv(A)
print("Inverse of A:\n", inverse_A)
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues of A:", eigenvalues)
print("Eigenvectors of A:\n", eigenvectors)


# # Ques 11
positions = np.array([[0, 0], [2, 3], [4, 7], [7, 10], [10, 15]])
# 11.1
distance = np.linalg.norm(positions[-1] - positions[0])
print("Euclidean Distance (start to end):", distance)
# 11.2
step_distances = np.linalg.norm(np.diff(positions, axis=0), axis=1)
total_distance = np.sum(step_distances)
print("Step-by-step distances:", step_distances)
print("Total Distance Traveled:", total_distance)


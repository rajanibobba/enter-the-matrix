from vector import Vector
from matrix import Matrix
from functools import reduce

# m1 = Matrix.random(3, 4)

# 1 cry
# 2 goto 1
# read in the matrix.txt
# filter the 4x2 and 2x4 matrices into
# different lists

mat_from_file_list = []
vectors = []

mat_four_by_two_list = []
mat_two_by_four_list = []
with open('matrix.txt') as f:
   for line in f:
       if (line != '\n'):
           vectors.append(Vector(*tuple(map(int, line.strip().split(' ')))))
       else:
           mat_from_file_list.append(Matrix(*tuple(vectors)))
           vectors = []
   mat_from_file_list.append(Matrix(*tuple(vectors)))

for mat in mat_from_file_list:
   if (mat.get_dim() == (4, 2)):
       mat_four_by_two_list.append(mat)
   else:
       mat_two_by_four_list.append(mat)

m421 = mat_four_by_two_list[0] 
m422 = mat_four_by_two_list[1]

m241 = mat_two_by_four_list[0]

# add any 2 compatible matrices
print(m421)
print(m422)
print(m421 + m422)

# multiply any 2 compatible matrices
print(m421.dot(m241))

# create a list of 5 3x3 matrices of random values
mat_list  = []
for i in range(5):
   mat_list.append(Matrix.random(3, 3))

#for m in mat_list:
#    print(m)     

# and add them together
#print("Final matrix after adding all random matrices")
final = reduce(lambda acc, mat: acc + mat, mat_list, Matrix(Vector(0, 0, 0), Vector(0, 0, 0), Vector(0, 0, 0)))
#print(final)

# scale any matrix
#print("Final matrix after scale by 3")
s3 = final.scale(3)
#print(fs3)

# multiply a matrix times a vector
m1 = mat_four_by_two_list[0]
#print("Matrix 1 ")
print(m1)
mv = m1.times_vector(Vector(2, 2, 2))
#rint(mv)

#transform a matrix
print("Transformed Matrix")
print(list(zip(*m1.vecs)))
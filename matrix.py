# create a matrix
# any dimension
# multiply 2 matrices
# add 2 matrices
# scale matrix
# create a random mxn matrix
# with values between 0 and 1
from vector import Vector
import random as rand
from functools import reduce
import itertools 

class Matrix:
   @staticmethod
   def random(r, c):
       m = []
       for i in range(r):
           r1 = Vector(*tuple([rand.random() for _ in range(c)]))
           m.append(r1)
       return Matrix(*tuple(m))

   def __init__(self, *vecs):
       self.vecs = vecs

   def __str__(self):
       output = reduce(lambda output, vec: output + str(vec) + '\n', self.vecs, '[') + ']'
       return output

   def __add__(self, other):
       return Matrix(*[c1 + c2 for c1, c2 in zip(self.vecs, other.vecs)])

   def scale(self, scalar):
       return Matrix(*[vec.scale(scalar) for vec in self.vecs])

   def get_dim(self):
       return len(self.vecs), len(self.vecs[0])

   def times_vector(self, vec):
        if (self.get_dim()[1] != len(vec)):
            return "Not Possible"
        else:    
            return([v.dot(vec) for v in self.vecs])

   def dot(self, other):
        if (self.get_dim()[1] != other.get_dim()[0]):
            return "Multiplication Not Possible"
        else:    
            return(1)

   def transform(self):
      return (list(zip(*self.vecs)))
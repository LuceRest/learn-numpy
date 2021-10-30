import numpy as np


a = np.array((  [1,2],
                [3,4]))

b = np.ones([2,2])

print("Matrix a :")
print(a)
print("-----------\n")

print("Matrix b :")
print(b)
print("-----------\n")


# -----------| Perkalian Matrix |-----------

c1 = np.dot(a,b)
c2 = a.dot(b)

print("Matrix c1 :")
print(c1)
print("-----------\n")

print("Matrix c2 :")
print(c2)
print("-----------\n")



'''
    NB :
        - numpy.dot()	~> Berfungsi untuk mengalikan dua matrix.
        - numpyt.dot(<matrix 1>, <matrix 2>)
        - <matrix 1>.dot(<matrix 2>)


'''


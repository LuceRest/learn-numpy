import numpy as np


A = np.array([(2,3), (1,2)])
Y = np.array([23, 14])

print()
print(A)
print()

print(Y)
print('\n----------------------\n')

A_inv = np.linalg.inv(A)


# -----------| Menyelesaikan Persamaan Linear |-----------

# Cara 1

X1 = np.dot(A_inv, Y)
print(X1)
print('\n----------------------\n')


# Cara 2

X2 = np.linalg.solve(A,Y)
print(X2)
print()



'''
    NB :
        - numpy.linalg.solve()	~> Berfungsi untuk menyelesaikan persamaan linear.
        - numpy.linalg.solve(<matrix 1>, <matrix 2>)


'''


import numpy as np


a = np.array([(1,-1), (1,1)])

print()
print(a)
print('\n----------------------\n')


# -----------| Invers Matrix |-----------

aInv = np.linalg.inv(a)
print(aInv)
print('\n----------------------\n')


# -----------| Determinan Matrix |-----------

aDet = np.linalg.det(a)
aDetInv = np.linalg.det(aInv)

print(aDet)
print('\n----------------------\n')

print(aDetInv)
print()



'''
    NB :
        - numpy.linalg.inv()	~> Berfungsi untuk menginvers suatu matrix.
        - numpy.linalg.inv(<matrix>)

        - numpy.linalg.det()	~> Berfungsi untuk menghitung determinan dari suatu matrix.
        - numpy.linalg.det(<matrix>)


'''



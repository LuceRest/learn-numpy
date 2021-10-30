import numpy as np


a = np.array([1,2,3])
b = np.array([4,5,6])

aMat = np.zeros((2,3))
bMat = np.ones((2,3))

print(a)
print()

print(b)
print()
print("----------------------\n")

print(aMat)
print()

print(bMat)
print()
print("----------------------\n")


# -----------| Stacking Matrix (Menumpuk Matrix) |-----------

c = np.hstack((a,b))
d = np.vstack((a,b))

cMat = np.hstack((aMat,bMat))
dMat = np.vstack((aMat,bMat))

print(c)
print()

print(d)
print()
print("----------------------\n")

print(cMat)
print()

print(dMat)
print()
print("----------------------\n")



'''
    NB :
        - numpy.hstack()		~> Berfungsi untuk menumpuk/menggabungkan matrix (staking matrix) secara horizontal (mendatar), namun barisnya harus sama.
        - numpy.hstack((<matrix 1>, <matrix 2>))

        - numpy.vstack()		~> Berfungsi untuk menumpuk/menggabungkan matrix (staking matrix) secara vertikal (menurun), namun kolomnya harus sama.
        - numpy.vstack((<matrix 1>, <matrix 2>))


'''




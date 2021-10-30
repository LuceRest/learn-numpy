import numpy as np


a1 = np.array([1,3])
b1 = np.array([3,0])


# -----------| Perkalian Dot |-----------

c1 = np.dot(a1, b1)

print()
print(c1)
print("\n----------------------\n")


# -----------| Perkalian Cross |-----------

a2 = np.array([1,2,0])
b2 = np.array([2,1,0])

c2 = np.cross(a2, b2)
print(c2)
print("\n----------------------\n")

c3 = np.cross(b2, a2)
print(c3)
print()



'''
    NB :
        - numpy.dot()	~> Berfungsi untuk melakukan perkalian dot pada dua buah matrix / vector yg hasilnya suatu bilangan.
        - numpy.dot(<matrix/vector 1>, <matrix/vector2>)

        - numpy.cross()	~> Berfungsi untuk melakukan perkalian cross pada dua buah matrix / vector yg hasilnya matrix / vector.
        - numpy.cross(<matrix/vector1>, <matrix/vector2>)


'''





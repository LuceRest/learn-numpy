import numpy as np


# -----------| Membuat Vector |-----------

a = np.array([1,2,3,4,5])
b = np.array([1.5, 2.5, 5, 6, 7])

print(a)
print(b)
print()


# -----------| Membuat Vector dengan Range |-----------

c = np.arange(1, 10, 2)

print(c)
print()

# -----------| Membuat Linspace |-----------

d = np.linspace(1, 10, 4)

print(d)
print()


# -----------| Membuat Array Multidimensi / Matrix |-----------

e = np.array( [ (1, 2, 3), (4, 5, 6) ] )

print(e)
print()


# -----------| Membuat Matrix dengan Nilai Nol |-----------

f = np.zeros((1,5))

print(f)
print()


# -----------| Membuat Matrix dengan Nilai Satu |-----------

g = np.ones((5,1))

print(g)
print()

# -----------| Membuat Matrix Identitas |-----------

h1 = np.identity(5)
h2 = np.eye(5)

print(h1)
print("------------------")
print(h2)
print()



'''
    NB :
        - numpy.array()		~> Berfungsi juga untuk membuat vector.
        - numpy.array([<nilai vector 1>, <nilai vector 2>, <nilai vector ...>]

        - numpy.arange()    ~> Berfungsi juga untuk membuat vector dengan range.
        - numpy.arange(<batas bawah>, <batas atas>, <range/jarak>)

        - numpy.linspace()	~> Berfungsi untuk membuat linspace / linear space.
        - numpy.linspace(<batas bawah>, <batas atas>, <jumlah nilai yg ingin ditampilkan dari batas bawah sampai atas>)

        - numpy.array()		~> Berfungsi juga untuk membuat matrix / array multidimensi.
        - numpy.array([ (<nilai baris 1>), (<nilai baris 2>), (<nilai baris ...>) ])

        - numpy.zeros()		~> Berfungsi untuk membuat matrix dengan nilai nol.
        - numpy.zeros((<jumlah baris>, <jumlah kolom>))

        - numpy.ones()		~> Berfungsi untuk membuat matrix dengan nilai satu.
        - numpy.ones((<jumlah baris>, <jumlah kolom>))

        - numpy.identity()	~> Berfungsi untuk membuat matrix identitas.
        - numpy.identity(<jumlah baris & kolom>)

        - numpy.eye()		~> Berfungsi untuk membuat matrix identitas.
        - numpy.eye(<jumlah baris & kolom>)


'''



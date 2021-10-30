import numpy as np


# -----------| Membuat Matrix dengan Tipe Data Tertentu |-----------

a = np.array(([1,2,3], [3,4,5]), dtype = float)

print(a)
print("\n----------------------\n")


# -----------| Membuat Array deengan Menggunakan Function |-----------

def kuadrat(baris, kolom):
    return kolom**2

def jumlah(baris, kolom):
    return (kolom + baris)

b = np.fromfunction(kuadrat, (1,10), dtype=int)

print(b)
print("\n----------------------\n")

c = np.fromfunction(jumlah, (4,4), dtype=float)

print(c)
print("\n----------------------\n")


# -----------| Membuat Array / Matrix dengan Menggunakan Iterable |-----------

iterable = (x*2 for x in range(5))

d = np.fromiter(iterable, dtype=int)

print(d)
print("\n----------------------\n")


# -----------| Multitype Array |-----------

dtipe = [('nama', 'S255'), ('tinggi', int)]

data = [
    ('Acil', 150),
    ('Evory', 160),
    ('Ebony', 180)
]

e = np.array(data, dtype=dtipe)

print(e)
print("\n----------------------\n")



'''
    NB :
        - numpy.array((<matrix>), dtype = <tipe data>)
            - dtype	~> Berfungsi untuk mengatur tipe datanya.

        - numpy.fromfunction()	~> Berfungsi untuk membuat array dengan menggunakan function.
        - numpy.fromfunction(<function>, (<baris>, <kolom>), dtype = <tipe data>)

        - numpy.fromiter()		~> Berfungsi untuk membuat array dengan menggunakan iteration.
        - numpy.fromiter(<iteration>, dtype = <tipe data>)

        - numpy.array()			~> Berfungsi juga untuk membuat array dengan multitype data.


'''


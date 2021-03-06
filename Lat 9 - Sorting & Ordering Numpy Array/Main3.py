import numpy as np


dtipe = [('Nama', 'S10'), ('Tinggi', int)]

data = [
    ('Acil', 170),
    ('Evory', 150),
    ('Ebony', 160)
]

a = np.array(data, dtype=dtipe)

print(a)
print("\n----------------------\n")

print(np.sort(a, order='Tinggi'))
print("\n----------------------\n")

print(np.sort(a, order='Nama'))
print()



'''
    NB :
        - numpy.random.randn()	~> Berfungsi untuk memunculkan array random.
        - numpy.random.randn(<baris>, <kolom>)

        - numpy.floor()			~> Berfungsi untuk membulatkan bilangan ke bawah.
        - numpy.floor(<bilangan/array>)

        - .max()				~> Berfungsi untuk mengambil nilai maksimal dari suatu array.
        - <array>.max()

        - .argmax()				~> Berfungsi untuk mengambil index dari nilai maksimal suatu array yang pertama kali ketemu.
        - <array>.argmax()

        - .min()				~> Berfungsi untuk mengambil nilai minimal dari suatu array.
        - <array>.min()

        - .argmin()				~> Berfungsi untuk mengambil index dari nilai minimal suatu array yang pertama kali ketemu.
        - <array>.argmin()

        - numpy.sort()			~> Berfungsi untuk mengurutkan suatu array dari nilai terkecil ke terbesar.
        - numpy.sort(<array>)

        - numpy.argsort()		~> Berfungsi untuk mengurutkan index suatu array dari index yg nilainya terkecil ke index yg nilainya terbesar.
        - numpy.argsort(<array>)

        - Sorting untuk array yg barisnya lebih dari satu, maka akan dilakukan sorting per baris.

        - numpy.sort(<array>, order = <acuan urutan>)
            - order	~> Berfungsi untuk acuan urutan saat mengurutkan suatu array.`


'''



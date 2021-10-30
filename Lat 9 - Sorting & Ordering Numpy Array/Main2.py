import numpy as np


a = np.floor(np.random.randn(2,2) * 10)

print('Nilai a :')
print(a)
print()

print('Nilai max dari a = ', a.max())
print('Posisi nilai max dari a = ', a.argmax())
print()

print('Nilai min dari a = ', a.min())
print('Posisi nilai min dari a = ', a.argmin())
print()

print('Mengurutkan nilai a :')
print(np.sort(a))
print(np.argsort(a))



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




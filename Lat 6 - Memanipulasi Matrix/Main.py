import numpy as np


a = np.array((
            [1,2,3],
            [4,5,6]
        ))

print('Matrix a dengan ukuran :', a.shape)
print(a)
print("---------------------------------\n")


# -----------| Transpose Matrix |-----------

print('Transpose matrix dari a :')
print(a.transpose())
print(a.T)
print('Matrix a dengan ukuran :', a.shape)
print("---------------------------------\n")


# -----------| Flatten Array (Vector Baris) |-----------

print('Flatten matrix a :')
print(a.ravel())
print(np.ravel(a))
print('Matrix a dengan ukuran :', a.shape)
print("---------------------------------\n")


# -----------| Reshape Matrix |-----------

print("Reshape matrix a :")
print(a.reshape(3,2))
print('Matrix a dengan ukuran :', a.shape)
print("---------------------------------\n")


# -----------| Resize Matrix |-----------

print("Resize matrix a :")
a.resize(3,2)
print(a)
print('Matrix a dengan ukuran :', a.shape)
print("---------------------------------\n")




'''
    NB :
        - <matrix numpy>.shape		    ~> Berfungsi untuk mengambil ukuran dari suatu matrix.

        - <matrix numpy>.transpose()	~> Berfungsi untuk melakukan transpose pada suatu matrix.
        - <matrix numpy>.transpose()
        - numpy.transpose(<matrix numpy>)
        - <matrix numpy>.T

        - <matrix numpy>.ravel()		~> Berfungsi untuk membuat suatu matrix menjadi vector baris / flatten array.
        - <matrix numpy>.ravel()
        - numpy.ravel(<matrix numpy>)

        - <matrix numpy>.reshape()		~> Berfungsi untuk merubah bentuk suatu matrix, namun jumlah isi komponen matrix masih tetap.
        - <matrix numpy>.reshape(<jumlah baris baru>, <jumlah kolom baru>)

        - <matrix numpy>.resize()		~> Berfungsi untuk merubah bentuk suatu matrix dan merubah variabel dari matrix numpy tsb, namun jumlah isi komponen matrix masih tetap.
        - <matrix numpy>.resize(<jumlah baris baru>, <jumlah kolom baru>)


'''

